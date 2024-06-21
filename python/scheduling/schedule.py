from scheduling.split_sche import make_split_scheduling
from io import TextIOWrapper
import sys, csv, time, os, argparse, importlib

args = sys.argv

def merge_dicts(table):
    new_table = {}
    for entry in table:
        new_table.update(entry)
    return new_table

def alpha2num(c):
    return ord(c) - ord("A")


def read_formula_csv(filename):
    f_read = open(filename, "r")
    formulas = []
    for line in csv.reader(f_read):
        if len(line) > 0 and line[0][0] == "#":
            continue
        if len(line) == 4:
            formulas.append([line[0], line[3], line[1], line[2]])
    f_read.close()
    return formulas


# c = a + b, e = c + d の時 e から c を探す
def find_prev_formula(formulas, operand):
    for formula in formulas:
        if formula[0] == operand:
            return formula
    return None


# c = a + b, e = c + d の時 c から e とスケジューリング結果を探して，最小／最大のサイクル数を返す
def find_next_formula(value, formulas, pre_sche_result):
    min_finish_time, max_finish_time = 1000, 0
    for formula in formulas:
        if (formula[2] == value) or (formula[3] == value):
            for sol in pre_sche_result:
                if formula[0] == sol[0]:
                    min_finish_time = min(min_finish_time, int(sol[2]))
                    max_finish_time = max(max_finish_time, int(sol[2]))
    return min_finish_time, max_finish_time


def find_prev_resource(pre_sche_result, operand):
    for pre in pre_sche_result:
        if pre[0] == operand:
            resource = pre[1][:-1]
            resource_num = pre[1][-1]
            end_time = int(pre[3])
            return resource, resource_num, end_time
    return None, None, None


def make_mem_task_definition(
    f_write: TextIOWrapper,
    input_value,
    pre_sche_result,
    formulas,
    mem_table,
    current_formula: list
):
    value = current_formula[0]
    if current_formula[2] == current_formula[3]:
        operands = [current_formula[2]]
    else:
        operands = [current_formula[2], current_formula[3]]

    for i in range(len(operands)):
        operand = operands[i]
        mem_value_name = "{0}_mem{1}".format(value, i)
        if operand in input_value:
            f_write.write("\t{0} = S.Task('{0}', length=1, delay_cost=1)\n".format(mem_value_name))
            f_write.write("\t{0} += INPUT_mem_r\n".format(mem_value_name))
        else:
            prev_formula = find_prev_formula(formulas, operand)
            pre_resource, pre_resource_num, pre_end_time = find_prev_resource(pre_sche_result, operand)
            if prev_formula is None:
                raise Exception("can't find previous formula")
            opcode = prev_formula[1]
            if opcode == "INV":
                f_write.write("\tS += {0} < {1}\n".format(operand, value))
                continue
            f_write.write("\t{0} = S.Task('{0}', length=1, delay_cost=1)\n".format(mem_value_name))
            if opcode == "MUL" or opcode == "ADD" or opcode == "SUB":
                if pre_resource is None:
                    f_write.write("\t{0} += alt(INPUT_mem_r)\n".format(mem_value_name))
                    f_write.write("\tS += {0}-1 < {1}\n".format(operand, mem_value_name))
                else:
                    f_write.write("\t{0} += INPUT_mem_r\n".format(mem_value_name))
                    f_write.write("\tS += {1} < {0}\n".format(mem_value_name, pre_end_time - 1))
            # if opcode == "MUL":
            #     if pre_resource is None:
            #         f_write.write("\t{0} += alt(MUL_mem)\n".format(mem_value_name))
            #         for j in range(MULnum):
            #             f_write.write("\tS += ({0}*MUL[{3}])-1 < {1}_mem{2}*MUL_mem[{3}]\n".format(operand, value, i, j))
            #     else:
            #         f_write.write("\t{0} += MUL_mem[{1}]\n".format(mem_value_name, pre_resource_num))
            #         f_write.write("\tS += {1} < {0}\n".format(mem_value_name, pre_end_time - 1))
            # elif opcode == "ADD" or opcode == "SUB":
            #     if pre_resource is None:
            #         f_write.write("\t{0} += alt(ADD_mem)\n".format(mem_value_name))
            #         for j in range(ADDnum):
            #             f_write.write("\tS += ({0}*ADD[{3}])-1 < {1}_mem{2}*ADD_mem[{3}]\n".format(operand, value, i, j))
            #     else:
            #         f_write.write("\t{0} += ADD_mem[{1}]\n".format(mem_value_name, pre_resource_num))
            #         f_write.write("\tS += {1} < {0}\n".format(mem_value_name, pre_end_time - 1))
        f_write.write("\tS += {1}-1 <= {0}\n\n".format(value, mem_value_name))
        mem_table[mem_value_name] = operand


def find_mistake(
    formulas, mem_table_list, output_value, split_ope, depth, pre_sche_result
):
    mistaken_formulas = []
    inv_val = ""
    for formula in split_ope[depth]:
        is_exist = False
        sub_value_results = []
        task = formula[0]
        sub_values = {
            key: False for key, value in mem_table_list[depth].items() if task in key
        }

        for sol in pre_sche_result:
            if task == sol[0]:
                is_exist = True
                task_result = sol
            elif sol[0] in sub_values.keys():
                sub_values[sol[0]] = True
                sub_value_results.append(sol)
        if not is_exist:
            for sub_value_result in sub_value_results:
                pre_sche_result.remove(sub_value_result)
            min_finish_time, max_finish_time = find_next_formula(
                task, formulas, pre_sche_result
            )
            mistaken_formulas.append(formula + [min_finish_time])
        elif False in sub_values.values():
            pre_sche_result.remove(task_result)
            for sub_value_result in sub_value_results:
                pre_sche_result.remove(sub_value_result)
            min_finish_time, max_finish_time = find_next_formula(
                task, formulas, pre_sche_result
            )
            mistaken_formulas.append(formula + [min_finish_time])
    print(mistaken_formulas)
    if depth + 1 >= len(split_ope):
        split_ope.append(mistaken_formulas)
    else:
        split_ope[depth + 1] = mistaken_formulas + split_ope[depth + 1]
    return pre_sche_result, split_ope


def make_pyschedule(
    dir_name,
    file_name,
    formulas,
    mem_table_list,
    split_ope,
    pre_sche_result,
    depth,
    input_value,
    output_value,
    MULnum,
    MULstage,
    ADDnum,
    read_num,
    input_num,
):

    f_write = open("{}/{}.py".format(dir_name, file_name), "w")
    f_write.write("from pyschedule import Scenario, solvers, plotters, alt\n\n\n")
    f_write.write("def solve():\n")

    # mul_cycle = mul_num_list[depth]
    # add_cycle = (add_num_list[depth] // ADDnum)

    # mul_cycle = mul_num_list[depth]
    # add_cycle = (add_num_list[depth] // ADDnum)
    pre_cycle = 0
    if pre_sche_result != []:
        pre_cycle = int(pre_sche_result[-1][3])
    f_write.write("\thorizon = {0}\n".format(max(pre_cycle + 90, input_num // 2 + 50)))

    f_write.write('\tS = Scenario("' + file_name + '", horizon=horizon)\n')

    f_write.write("\n\t# resource\n")
    f_write.write("\tMUL = S.Resources('MUL', num={0}, size={1})\n".format(MULnum, MULstage))
    f_write.write("\tMUL_in = S.Resources('MUL_in', num={0})\n".format(MULnum))
    f_write.write("\tINV = S.Resource('INV')\n")
    f_write.write(
        "\tADD = S.Resources('ADD', num={0}, periods=range(1, horizon))\n".format(
            ADDnum
        )
    )
    f_write.write(
        "\tSUB = S.Resources('SUB', num={0}, periods=range(1, horizon))\n".format(
            ADDnum
        )
    )

    # # 1write-2read RAM
    # f_write.write(
    #     "\tMUL_mem = S.Resources('MUL_mem', num={0}, size=2)\n".format(MULnum)
    # )
    # f_write.write(
    #     "\tADD_mem = S.Resources('ADD_mem', num={0}, size=2)\n".format(ADDnum)
    # )

    # 2write-2read RAM
    f_write.write("\tINPUT_mem_w = S.Resource('INPUT_mem_w', size=2)\n")
    f_write.write("\tINPUT_mem_r = S.Resource('INPUT_mem_r', size={})\n".format(read_num))

    multi_resources = ["MUL", "MUL_in", "ADD"]
    # multi_resources = ["MUL", "MUL_in", "ADD", "MUL_mem", "ADD_mem"]
    single_resources = ["INV", "INPUT_mem_w", "INPUT_mem_r"]

    f_write.write("\n\t# result of previous scheduling\n")

    for pre in pre_sche_result:
        task = pre[0]
        start_time = int(pre[2])
        end_time = int(pre[3])
        length = end_time - start_time
        f_write.write(
            "\t{0} = S.Task('{0}', length={1}, delay_cost=1)\n".format(task, length)
        )
        f_write.write("\tS += {0} >= {1}\n".format(task, start_time))
        if pre[1] in single_resources:
            f_write.write("\t{0} += {1}\n\n".format(task, pre[1]))
        else:
            resource = pre[1][:-1]
            resource_num = pre[1][-1]
            f_write.write("\t{0} += {1}[{2}]\n\n".format(task, resource, resource_num))

    f_write.write("\n\t# new tasks\n")
    tmp_mem_table = {}
    for line in split_ope[depth]:
        if line[1] == "MUL":
            f_write.write(
                "\t{0}_in = S.Task('{0}_in', length=1, delay_cost=1)\n".format(line[0])
            )
            f_write.write("\t" + line[0] + "_in += alt(MUL_in)\n")
            f_write.write(
                "\t{0} = S.Task('{0}', length={1}, delay_cost=1)\n".format(line[0], MULstage)
            )
            f_write.write("\t" + line[0] + " += alt(MUL)\n")
            f_write.write("\tS += {0}>={0}_in\n\n".format(line[0]))
        elif line[1] == "ADD":
            f_write.write(
                "\t{0} = S.Task('{0}', length=1, delay_cost=1)\n".format(line[0])
            )
            f_write.write("\t" + line[0] + " += alt(ADD)\n\n")
        elif line[1] == "SUB":
            f_write.write(
                "\t{0} = S.Task('{0}', length=1, delay_cost=1)\n".format(line[0])
            )
            f_write.write("\t" + line[0] + " += alt(SUB)\n\n")
        elif line[1] == "INV":
            f_write.write(
                "\t{0} = S.Task('{0}', length=1, delay_cost=1)\n".format(line[0])
            )
            f_write.write("\t" + line[0] + " += alt(INV)\n\n")
        else:
            raise Exception("ERROR: invalid operand: " + line[1])
        if line[0] in output_value:
            if "new_" in line[0]:
                min_finish_time, max_finish_time = find_next_formula(
                    line[0][4:], formulas, pre_sche_result
                )
            else:
                min_finish_time_1, max_finish_time_1 = find_next_formula(
                    "a{}".format(line[0][1:]), formulas, pre_sche_result
                )
                min_finish_time_2, max_finish_time_2 = find_next_formula(
                    "b{}".format(line[0][1:]), formulas, pre_sche_result
                )
                max_finish_time = max(max_finish_time_1, max_finish_time_2)
            f_write.write("\tS += {}<{}\n\n".format(max_finish_time, line[0]))
        if len(line) == 5:
            f_write.write("\tS += {}<{}\n\n".format(line[0], line[4]))
        make_mem_task_definition(
            f_write,
            input_value,
            pre_sche_result,
            formulas,
            tmp_mem_table,
            line
        )
        if line[0] in output_value:
            f_write.write("\t{0}_w = S.Task('{0}_w', length=1, delay_cost=1)\n".format(line[0]))
            f_write.write("\t{0}_w += alt(INPUT_mem_w)\n".format(line[0]))
            f_write.write("\tS += {0}-1 <= {0}_w\n\n".format(line[0]))
    mem_table_list.append(tmp_mem_table)

    f_write.write("\tsolvers.mip.solve(S,msg=1,ratio_gap=1.01)\n\n")
    # f_write.write("\tsolvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)\n\n")
    f_write.write(
        "\tsolution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]\n"
    )
    f_write.write(
        "\tfor i in range(len(S.solution())):\n\t\tfor j in range(len(S.solution()[i])):\n\t\t\tsolution[i][j]=str(S.solution()[i][j])\n"
    )
    f_write.write("\tprint(solution)\n\n")
    f_write.write("\tcycles = int(solution[-1][3])\n\n")

    # TODO: pic_file_nameの変更
    f_write.write('\tpic_file_name = "{}/{}.png"\n'.format(dir_name, file_name))
    f_write.write(
        "\tif(S.solution() != []):\n\t\tplotters.matplotlib.plot(S,img_filename=pic_file_name, vertical_text=True, fig_size=(cycles*0.25+3, 5))\n\n"
    )
    f_write.write("\treturn solution\n\n")
    return


if __name__ == "__main__":
    start_time = time.perf_counter()
    psr = argparse.ArgumentParser(
        usage="schedule.py -c <curve_group> -p <p[bit]>",
        description="Execute scheduling with a 7-stage pipelined Fp montgomery multiplier, four Fp adders/subtractors, an Fp inversion operator",
    )
    psr.add_argument(
        "-mn",
        "--mulNum",
        default=1,
        help="number of Fp montgomery multipliers (default is 1)",
    )
    psr.add_argument(
        "-ms",
        "--mulStage",
        required=True,
        help="number of stages of Fp montgomery multipliers",
    )
    psr.add_argument(
        "-a", "--addNum", default=4, help="number of Fp adders/subtractors (default is 4)"
    )
    psr.add_argument(
        "-rn", "--readNum", default=4, help="number of RAM read ports (default is 4)"
    )
    # psr.add_argument("-c", "--curve", required=True, help="curve group")
    # psr.add_argument(
    #     "-p",
    #     "--characteristic",
    #     required=True,
    #     help="bit width of characteristic number p",
    # )
    psr.add_argument("-n", "--name", required=True, help="スケジューリング対象の名前")
    args = psr.parse_args()

    mul_num = int(args.mulNum)
    mul_stage = int(args.mulStage)
    add_num = int(args.addNum)
    read_num = int(args.readNum)
    # curve_group = args.curve
    # curve_name = args.characteristic
    algo_name = args.name

    func_name = "{2}_mul{0}_add{1}".format(mul_num, add_num, algo_name)
    formulas = read_formula_csv(
        "/Users/fukudamomoko/Desktop/research/ABE/python/scheduling/{}.csv".format(algo_name)
    )

    # exec(open("./" + "sche_test.py", 'r', encoding="utf-8").read())
    file_name = func_name

    # スケジューリングの解を保存するリスト
    solution = []
    # 分割したfomulas
    split_ope, input_value, output_value, input_num = make_split_scheduling(formulas)
    print("input = ", end="")
    print(input_value)
    print("output = ", end="")
    print(output_value)
    split_ope.append([])
    os.makedirs(file_name, exist_ok=True)

    for i in range(len(split_ope)):
        print(i, len(split_ope[i]), split_ope[i])

    pre_sche_result = solution
    mem_table_list = []
    print(len(split_ope))
    for i in range(len(split_ope)):
        # pre_sche_result, split_ope = find_mistake(split_ope, i, pre_sche_result)
        if len(split_ope[i]) == 0:
            continue
        write_file = "{0}_{1}".format(file_name, i)
        make_pyschedule(
            file_name,
            write_file,
            formulas,
            mem_table_list,
            split_ope,
            pre_sche_result,
            i,
            input_value,
            output_value,
            mul_num,
            mul_stage,
            add_num,
            read_num,
            input_num)
        print(i)
        # print(split_ope[i])
        # make_pyschedule(file_name, formulas, mem_table, split_ope, pre_sche_result, i, write_file, input_value, mul_num, add_num, mul_num_list, add_num_list, input_num)
        scheduling_i = importlib.import_module("{}.{}".format(file_name, write_file))
        solution = scheduling_i.solve()
        if solution == []:
            raise Exception("no solution found in schedule_{0}".format(i))
        pre_sche_result = solution

    end_time = time.perf_counter()
    
    mem_table = merge_dicts(mem_table_list)

    f = open(file_name + ".txt", "w")
    print("input = ", file=f, end="")
    print(input_value, file=f)
    print("output = ", file=f, end="")
    print(output_value, file=f)
    print("solution = ", file=f, end="")
    print(solution, file=f)
    print("formulas = ", file=f, end="")
    print(formulas, file=f)
    print("mem_table = ", file=f, end="")
    print(mem_table, file=f)
    print("time = ", end_time - start_time)

    for filename in os.listdir("./"):
        if filename.endswith(".log") and "clone" in filename:
            file_path = os.path.join("./", filename)
            os.remove(file_path)
    os.remove("./Integer_Program-pulp.lp")
    os.remove("./Integer_Program-pulp.sol")
