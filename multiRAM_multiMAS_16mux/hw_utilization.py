import csv, os
from formula_data import formulaData

def calc_hw_utilization(solution, mul_num: int, add_num: int):
# def calc_hw_utilization(algo_name:str, mul_num:int, mul_stage:int, add_num:int, add_stage:int):
    # config = "stage{ms}MM{mn}_stage{as_}MAS{an}".format(mn=mul_num, ms=mul_stage, an=add_num, as_=add_stage)
    # solution = []
    # result_file_path = "./scheduling_result/{}/{}/result.txt".format(config, algo_name)
    #     # read scheduling result file
    # namespace = {}
    # input = []

    # print(result_file_path)
    # exec(open(result_file_path, 'r', encoding="utf-8").read())

    # print(input)
    total_cycle = int(solution[-1][-1])

    util_list = {}
    for i in range(mul_num):
        util_list["MM{}".format(i)] = 0
    for i in range(add_num):
        util_list["MAS{}".format(i)] = 0

    for sol in solution:
        if sol[1] in util_list.keys():
            util_list[sol[1]] += 1

    res = {}
    for opr, util_num in util_list.items():
        if "MM" in opr:
            res[opr] = round(util_num / (total_cycle - mul_stage), 2)
        else:
            res[opr] = round(util_num / (total_cycle - add_stage), 2)

    return res

    # result_file = open(result_file_path, 'a', encoding="utf-8")
    # print("utilization = ", file=result_file, end="")
    # print(res, file=result_file, end="")

def read_formula_csv(filename) -> list[formulaData]:
    f_read = open(filename, "r")
    formulas = []
    for line in csv.reader(f_read):
        if (len(line) > 0 and line[0][0] == "#") or len(line) < 3:
            continue
        if line[-1] == "CSEL":
            formula = formulaData(operands=line[1:4], result=line[0], type = line[-1])
        else:
            if line[1] == line[2]:
                formula = formulaData(operands=[line[1]], result=line[0], type = line[-1])
            else:
                formula = formulaData(operands=line[1:3], result=line[0], type = line[-1])
        formulas.append(formula)
    f_read.close()
    return formulas

def fix_formulas(algo_name:str, mul_num:int, mul_stage:int, add_num:int, add_stage:int):
    formulas = read_formula_csv(
        "{}/csv/{}.csv".format(os.path.dirname(os.path.dirname(__file__)), algo_name)
    )
    config = "stage{ms}MM{mn}_stage{as_}MAS{an}".format(mn=mul_num, ms=mul_stage, an=add_num, as_=add_stage)
    result_file_path = "./scheduling_result/{}/{}/result.txt".format(config, algo_name)

    lines = open(result_file_path, 'r', encoding="utf-8").readlines()

    f = open("./scheduling_result/{}/{}/result.txt".format(config, algo_name), 'w', encoding="utf-8")
    f.writelines(lines[:3] + [lines[4]])
    # print(lines[1])
    # print(lines[2])
    # print(lines[4])

    print("formulas = [", file=f, end="")
    for formula in formulas:
        formula.print(file=f, end=("]\n" if formula == formulas[-1] else ", "))
    f.close()

# fix_formulas("CONJ", 1, 8, 4, 3)

if __name__ == "__main__":
    algo_name = "EP2_ADD_w_EVAL"
    mul_stage = 5
    add_stage = 2
    # fix_formulas(algo_name, 1, mul_stage, 4, add_stage)
    config = "stage{ms}MM{mn}_stage{as_}MAS{an}".format(mn=1, ms=mul_stage, an=4, as_=add_stage)
    solution = []
    result_file_path = "./scheduling_result/{}/{}/result.txt".format(config, algo_name)
        # read scheduling result file
    namespace = {}

    exec(open(result_file_path, 'r', encoding="utf-8").read())
    res = calc_hw_utilization(solution, 1, 4)

    result_file = open(result_file_path, 'a', encoding="utf-8")
    print("utilization = ", file=result_file, end="")
    print(res, file=result_file, end="\n")
    # all_res = []
    # for mul_stage in range(4, 9):
    #     for add_stage in range(1, 4):
    #         for algo_name in ["CONJ", "FROB", "MUL", "EP2_ADD_w_EVAL", "EP2_DBL_w_EVAL", "SPARSE", "SQR", "SQR012345", "EP_ADD_A_0", "EP_ADD_A_ANY", "EP_DBL_A_0", "ISOGENY", "FP12_INV_BEFORE_FPINV", "FP12_INV_AFTER_FPINV", "2xSSWU_BEFORE_EXP", "2xSSWU_AFTER_EXP", "EP_LADDERMUL", "EP_YRECOVER", "EP2_LADDERMUL", "EP2_YRECOVER", "FP12_LADDERMUL"]:
    #             try:
    #                 fix_formulas(algo_name, 1, mul_stage, 4, add_stage)
    #                 config = "stage{ms}MM{mn}_stage{as_}MAS{an}".format(mn=1, ms=mul_stage, an=4, as_=add_stage)
    #                 solution = []
    #                 result_file_path = "./scheduling_result/{}/{}/result.txt".format(config, algo_name)
    #                     # read scheduling result file
    #                 namespace = {}

    #                 exec(open(result_file_path, 'r', encoding="utf-8").read())
    #                 res = calc_hw_utilization(solution, 1, 4)

    #                 result_file = open(result_file_path, 'a', encoding="utf-8")
    #                 print("utilization = ", file=result_file, end="")
    #                 print(res, file=result_file, end="\n")
    #                 res_tmp = [algo_name]
    #                 for value in res.values():
    #                     res_tmp.append(value)
    #                 all_res.append(res_tmp)
    #             except:
    #                 pass
    
    # with open("all_utilization.csv", mode='w', newline='') as file:
    #     writer = csv.writer(file)
    #     for row in all_res:
    #         writer.writerow(row)

# for mul_stage in range(4, 9):
#     for add_stage in range(1, 4):
#         fix_formulas("CONJ", 1, 8, 4, 3)