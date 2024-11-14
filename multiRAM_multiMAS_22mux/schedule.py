from split_sche import make_split_scheduling
from io import TextIOWrapper
import sys, csv, time, os, argparse, importlib
from formula_data import formulaData

args = sys.argv


def merge_dicts(table):
    new_table = {}
    for entry in table:
        new_table.update(entry)
    return new_table

def alpha2num(c):
    return ord(c) - ord("A")


def read_formula_csv(filename) -> list[formulaData]:
    f_read = open(filename, "r")
    formulas = []
    for line in csv.reader(f_read):
        if len(line) > 0 and line[0][0] == "#":
            continue
        if line[-1] == "CSEL":
            formula = formulaData(operands=line[1:4], result=line[0], type = line[-1])
        else:
            if line[1] == line[2]:
                formula = formulaData(operands=line[1], result=line[0], type = line[-1])
            else:
                formula = formulaData(operands=line[1:3], result=line[0], type = line[-1])
        formulas.append(formula)
    f_read.close()
    return formulas


# c = a + b, e = c + d の時 e から c を探す
def find_prev_formula(formulas: list[formulaData], operand):
    for formula in formulas:
        if formula.result == operand:
            return formula
    raise Exception("can't find previous formula of %s" % formula.result)


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
            resource_num = int(pre[1][-1])
            end_time = int(pre[3])
            return resource, resource_num, end_time
    return None, None, None


def make_mem_task_definition(
        f_write: TextIOWrapper,
        input_value,
        pre_sche_result,
        formulas,
        mem_table,
        target_formula: formulaData,
        MMnum: int,
        MASnum: int):
    # value = current_formula[0]
    # if current_formula[-1] == "CSEL":
    #     operands = [current_formula[2], current_formula[3], current_formula[4]]
    # elif current_formula[2] == current_formula[3]:
    #     operands = [current_formula[2]]
    # else:
    #     operands = [current_formula[2], current_formula[3]]
    
    for i in range(len(target_formula.operands)):
        operand = target_formula.operands[i]
        mem_value_name = "{0}_mem{1}".format(target_formula.result, i)
        if operand in input_value:
            f_write.write("\t{0} = S.Task('{0}', length=1, delay_cost=1)\n".format(mem_value_name))
            f_write.write("\t{0} += MAIN_MEM_r\n".format(mem_value_name))
        else:
            prev_formula = find_prev_formula(formulas, operand)
            opcode = prev_formula.type
            if opcode == "INV" or opcode == "CSEL":
                f_write.write("\tS += {0} < {1}\n".format(operand, target_formula.result))
                continue
            pre_resource, pre_resource_num, pre_end_time = find_prev_resource(pre_sche_result, operand)
            if prev_formula is None:
                raise Exception("can't find previous formula")
            f_write.write("\t{0} = S.Task('{0}', length=1, delay_cost=1)\n".format(mem_value_name))
            if opcode == "MUL":
                if pre_resource is None:
                    f_write.write("\t{0} += alt(MM_MEM)\n".format(mem_value_name))
                    for j in range(MMnum):
                        f_write.write("\tS += ({0}*MM[{3}])-1 < {1}_mem{2}*MM_MEM[{3}]\n".format(operand, target_formula.result, i, j))
                else:
                    f_write.write("\t{0} += MM_MEM[{1}]\n".format(mem_value_name, pre_resource_num))
                    f_write.write("\tS += {1} < {0}\n".format(mem_value_name, pre_end_time - 1))
            elif opcode == "ADD" or opcode == "SUB":
                if pre_resource is None:
                    f_write.write("\t{0} += alt(MAS_MEM)\n".format(mem_value_name))
                    for j in range(MASnum):
                        f_write.write("\tS += ({0}*MAS[{3}])-1 < {1}_mem{2}*MAS_MEM[{3}]\n".format(operand, target_formula.result, i, j))
                else:
                    f_write.write("\t{0} += MAS_MEM[{1}]\n".format(mem_value_name, pre_resource_num))
                    f_write.write("\tS += {1} < {0}\n".format(mem_value_name, pre_end_time - 1))
        f_write.write("\tS += {1} <= {0}\n\n".format(target_formula.result, mem_value_name))
        mem_table[mem_value_name] = operand


def find_mistake(formulas: list[formulaData], mem_table_list, output_value, split_ope: list[list[formulaData]], depth: int, pre_sche_result):
    mistaken_formulas = []
    for formula in split_ope[depth]:
        is_exist = False
        sub_value_results = []
        task = formula.result
        # sub_values = {"{}_mem0".format(task): False, "{}_mem1".format(task): False}
        sub_values = {key: False for key, value in mem_table_list[depth].items() if task in key}
        if task in output_value:
            sub_values["{}_w".format(task)] = False
        if formula.type == "MUL":
            sub_values["{}_in".format(task)] = False

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
            min_finish_time, max_finish_time = find_next_formula(task, formulas, pre_sche_result)
            formula.set_limit_time(min_finish_time)
            mistaken_formulas.append(formula)
        elif False in sub_values.values():
            pre_sche_result.remove(task_result)
            for sub_value_result in sub_value_results:
                pre_sche_result.remove(sub_value_result)
            min_finish_time, max_finish_time = find_next_formula(task, formulas, pre_sche_result)
            formula.set_limit_time(min_finish_time)
            mistaken_formulas.append(formula)
    print(mistaken_formulas)
    if depth+1 >= len(split_ope):
        split_ope.append(mistaken_formulas)
    else:
        split_ope[depth+1] = mistaken_formulas + split_ope[depth+1]
    return pre_sche_result, split_ope



def make_pyschedule(
    dir_name,
    formulas,
    mem_table_list,
    split_ope: list[list[formulaData]],
    pre_sche_result,
    depth: int,
    input_value,
    output_value,
    MMnum,
    MMstage,
    MASnum,
    MASstage,
    input_num,
):

    f_write = open("{}/schedule{}.py".format(dir_name, depth), "w")
    f_write.write("from pyschedule import Scenario, solvers, plotters, alt\n\n\n")
    f_write.write("def solve():\n")

    # mul_cycle = mul_num_list[depth]
    # add_cycle = (add_num_list[depth] // MASnum)

    # mul_cycle = mul_num_list[depth]
    # add_cycle = (add_num_list[depth] // MASnum)
    pre_cycle = 0
    if pre_sche_result != []:
        pre_cycle = int(pre_sche_result[-1][3])
    f_write.write("\thorizon = {0}\n".format(max(pre_cycle + 90, input_num // 2 + 50)))

    f_write.write('\tS = Scenario("schedule{}", horizon=horizon)\n'.format(depth))

    f_write.write("\n\t# resource\n")
    f_write.write("\tMM = S.Resources('MM', num={0}, size={1})\n".format(MMnum, MMstage))
    f_write.write("\tMM_in = S.Resources('MM_in', num={0})\n".format(MMnum))
    f_write.write("\tCSEL = S.Resource('CSEL')\n")
    f_write.write("\tINV = S.Resource('INV')\n")
    f_write.write(
        "\tMAS = S.Resources('MAS', num={0}, size={1}, periods=range(1, horizon))\n".format(
            MASnum, MASstage
        )
    )

    # 1write-2read RAM
    f_write.write(
        "\tMM_MEM = S.Resources('MM_MEM', num={0}, size=2)\n".format(MMnum)
    )
    f_write.write(
        "\tMAS_MEM = S.Resources('MAS_MEM', num={0}, size=2)\n".format(MASnum)
    )

    # 2write-2read RAM
    f_write.write("\tMAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)\n")
    f_write.write("\tMAIN_MEM_r = S.Resource('MAIN_MEM_r', size=2)\n")

    multi_resources = ["MM", "MM_in", "MAS", "MM_MEM", "MAS_MEM"]
    single_resources = ["INV", "MAIN_MEM_w", "MAIN_MEM_r"]

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
    for target_formula in split_ope[depth]:
        if target_formula.type == "MUL":
            f_write.write(
                "\t{0}_in = S.Task('{0}_in', length=1, delay_cost=1)\n".format(target_formula.result)
            )
            f_write.write("\t" + target_formula.result + "_in += alt(MM_in)\n")
            f_write.write(
                "\t{0} = S.Task('{0}', length={1}, delay_cost=1)\n".format(target_formula.result, MMstage)
            )
            f_write.write("\t" + target_formula.result + " += alt(MM)\n")
            f_write.write("\tS += {0}>={0}_in\n\n".format(target_formula.result))
        elif target_formula.type == "ADD" or target_formula.type == "SUB":
            f_write.write(
                "\t{0} = S.Task('{0}', length={1}, delay_cost=1)\n".format(target_formula.result, MASstage)
            )
            f_write.write("\t" + target_formula.result + " += alt(MAS)\n\n")
        elif target_formula.type == "INV":
            f_write.write(
                "\t{0} = S.Task('{0}', length=1, delay_cost=1)\n".format(target_formula.result)
            )
            f_write.write("\t" + target_formula.result + " += alt(INV)\n\n")

        elif target_formula.type == "CSEL":
            f_write.write(
                "\t{0} = S.Task('{0}', length=3, delay_cost=1)\n".format(target_formula.result)
            )
            f_write.write("\t" + target_formula.result + " += alt(CSEL)\n\n")
        else:
            raise Exception("ERROR: invalid operand: " + target_formula.type)
        if target_formula.result in output_value:
            if "new_" in target_formula.result:
                min_finish_time, max_finish_time = find_next_formula(
                    target_formula.result[4:], formulas, pre_sche_result
                )
            else:
                min_finish_time_1, max_finish_time_1 = find_next_formula(
                    "a{}".format(target_formula.result[1:]), formulas, pre_sche_result
                )
                min_finish_time_2, max_finish_time_2 = find_next_formula(
                    "b{}".format(target_formula.result[1:]), formulas, pre_sche_result
                )
                max_finish_time = max(max_finish_time_1, max_finish_time_2)
            f_write.write("\tS += {}<{}\n\n".format(max_finish_time, target_formula.result))
            f_write.write("\t{0}_w = S.Task('{0}_w', length=1, delay_cost=1)\n".format(target_formula.result))
            f_write.write("\t{0}_w += alt(MAIN_MEM_w)\n".format(target_formula.result))
            f_write.write("\tS += {0} <= {0}_w\n\n".format(target_formula.result))
        if target_formula.limit_time != -1:
            f_write.write("\tS += {}<{}\n\n".format(target_formula.result, target_formula.limit_time))
        make_mem_task_definition(
            f_write,
            input_value,
            pre_sche_result,
            formulas,
            tmp_mem_table,
            target_formula,
            MMnum,
            MASnum
        )
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
    f_write.write('\tpic_file_name = "{}/schedule{}.png"\n'.format(dir_name, depth))
    # f_write.write(
    #     "\tif(S.solution() != []):\n\t\tplotters.matplotlib.plot(S,img_filename=pic_file_name, fig_size=(cycles*0.25+3, 5))\n\n"
    # )
    f_write.write(
        "\tif(S.solution() != []):\n\t\tplotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 5))\n\n"
    )
    f_write.write("\treturn solution\n\n")
    return



if __name__ == "__main__":
    start_time = time.perf_counter()
    psr = argparse.ArgumentParser(
        usage="schedule.py -mn <number_of_MM> -ms <stages_of_MM> -an <number_of_MAS> -as <stages_of_MAS>",
        description="Execute scheduling with a 7-stage pipelined Fp montgomery multiplier, four Fp adders/subtractors, an Fp inversion operator",
    )
    psr.add_argument(
        "-mn",
        "--mulNum",
        default=1,
        help="number of Modular Multiplier (default is 1)",
    )
    psr.add_argument(
        "-ms",
        "--mulStage",
        required=True,
        help="number of stages of Modular Multiplier",
    )
    psr.add_argument(
        "-an", "--addNum", default=1, help="number of Modular Adders/Subtractors (default is 4)"
    )
    psr.add_argument(
        "-as",
        "--addStage",
        required=True,
        help="number of stages of Modular Adder/Subtractor",
    )
    # psr.add_argument("-n", "--name", required=True, help="スケジューリング対象の名前")
    args = psr.parse_args()

    mul_num = int(args.mulNum)
    mul_stage = int(args.mulStage)
    add_num = int(args.addNum)
    add_stage = int(args.addStage)
    # curve_group = args.curve
    # curve_name = args.characteristic
    # algo_name = args.name

    config = "stage{ms}MM{mn}_stage{as_}MAS{an}".format(mn=mul_num, ms=mul_stage, an=add_num, as_=add_stage)


    def exec_split_scheduling(algo_name):
        formulas = read_formula_csv(
            "{}/csv/{}.csv".format(os.path.dirname(os.path.dirname(__file__)), algo_name)
        )

        dir_name = "{directory}/scheduling_result/{config}/{algo}".format(directory=os.getcwd(),config=config, algo=algo_name)

        # スケジューリングの解を保存するリスト
        # 分割したfomulas
        split_ope, input_value, output_value, input_num = make_split_scheduling(formulas)
        os.makedirs(dir_name, exist_ok=True)
        f = open(dir_name + "/result.txt", "w")
        print("input = ", file=f, end="")
        print(input_value, file=f)
        print("output = ", file=f, end="")
        print(output_value, file=f)
        split_ope.append([])

        for i in range(len(split_ope)):
            print(i, len(split_ope[i]))
            for split_opei_data in split_ope[i]:
                split_opei_data.print()

        solution = []
        pre_sche_result = solution
        mem_table_list = []
        print(len(split_ope))

        cnt = 0
        while cnt < len(split_ope):
            if len(split_ope[cnt]) == 0:
                break
            make_pyschedule(
                dir_name,
                formulas,
                mem_table_list,
                split_ope,
                pre_sche_result,
                cnt,
                input_value,
                output_value,
                mul_num,
                mul_stage,
                add_num,
                add_stage,
                input_num)
            print(cnt)
            # print(split_ope[i])
            # make_pyschedule(file_name, formulas, mem_table, split_ope, pre_sche_result, i, write_file, input_value, mul_num, add_num, mul_num_list, add_num_list, input_num)
            scheduling_i = importlib.import_module("scheduling_result.{}.{}.schedule{}".format(config, algo_name, cnt))
            solution = scheduling_i.solve()
            if solution == []:
                raise Exception("no solution found in schedule_{0}".format(cnt))
            pre_sche_result = solution
            pre_sche_result, split_ope = find_mistake(formulas, mem_table_list, output_value, split_ope, cnt, pre_sche_result)
            cnt += 1

        end_time = time.perf_counter()
        
        mem_table = merge_dicts(mem_table_list)

        print("solution = ", file=f, end="")
        print(solution, file=f)
        print("formulas = [", file=f, end="")
        for formula in formulas:
            formula.print(file=f)
        print("]\nmem_table = ", file=f, end="")
        print(mem_table, file=f)
        f.close()
        print("time = ", end_time - start_time)

    for algo_name in ["EP_ADD_A_0"]:
        exec_split_scheduling(algo_name)
    # for algo_name in ["CONJ", "FROB", "MUL", "PADD", "PDBL", "SPARSE", "SQR", "SQR012345", "INV"]:
    #     exec_split_scheduling(algo_name)

    for filename in os.listdir("./"):
        if filename.endswith(".log") and "clone" in filename:
            file_path = os.path.join("./", filename)
            os.remove(file_path)
    os.remove("./Integer_Program-pulp.lp")
    os.remove("./Integer_Program-pulp.sol")
