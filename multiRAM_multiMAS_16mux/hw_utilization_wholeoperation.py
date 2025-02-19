import csv, os, pandas
from formula_data import formulaData

def count_occupied_cycles(solution, mul_stage: int, mul_num: int, add_stage: int, add_num: int):
    util_list = {}
    for i in range(mul_num):
        util_list["MM{}".format(i)] = mul_stage - 1
    for i in range(add_num):
        util_list["MAS{}".format(i)] = add_stage - 1

    for sol in solution:
        if sol[1] in util_list.keys():
            util_list[sol[1]] += 1

    return util_list


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


if __name__ == "__main__":

    G1_results_df = pandas.DataFrame()
    G2_results_df = pandas.DataFrame()
    m2c_results_df = pandas.DataFrame()
    pairing_results_df = pandas.DataFrame()
    GT_results_df = pandas.DataFrame()
    
    for mul_stage in [5,6,7,8,10,13]:
        for add_num in range(1, 6):
            try:
                add_stage = 1 if mul_stage < 10 else 2
                util_list = {}
                total_cycle_list = {}
                config = "stage{ms}MM{mn}_stage{as_}MAS{an}".format(mn=1, ms=mul_stage+1, an=add_num, as_=add_stage+1)
                for algo_name in ["CONJ", "FROB", "MUL", "EP2_ADD_w_EVAL", "EP2_DBL_w_EVAL", "SPARSE", "SQR", "SQR012345", "EP_ADD_A_0", "EP_ADD_A_ANY", "EP_DBL_A_0", "ISOGENY", "FP12_INV_BEFORE_FPINV", "FP12_INV_AFTER_FPINV", "2xSSWU_BEFORE_EXP", "2xSSWU_AFTER_EXP", "EP_LADDERMUL", "EP_YRECOVER", "EP2_LADDERMUL", "EP2_YRECOVER", "FP12_LADDERMUL"]:
                    solution = []
                    result_file_path = "./scheduling_result/{}/{}/result.txt".format(config, algo_name)
                        # read scheduling result file
                    namespace = {}

                    exec(open(result_file_path, 'r', encoding="utf-8").read())
                    util_list[algo_name] = count_occupied_cycles(solution, mul_stage=mul_stage, mul_num=1, add_stage=add_stage+1, add_num=add_num)
                    total_cycle_list[algo_name] =  int(solution[-1][-1])
                
                #  G1 scalar mul
                results_df = pandas.Series(index=util_list["CONJ"].keys(), name=config)
                total_cycle = total_cycle_list["EP_LADDERMUL"]*255 + total_cycle_list["EP_YRECOVER"]
                for operator in util_list["CONJ"].keys():
                    occupied_cycle = util_list["EP_LADDERMUL"][operator]*255 + util_list["EP_YRECOVER"][operator]
                    results_df.loc[operator] = occupied_cycle / total_cycle
                G1_results_df = pandas.concat([G1_results_df, results_df], axis=1)
                
                #  G2 scalar mul
                results_df = pandas.Series(index=util_list["CONJ"].keys(), name=config)
                total_cycle = total_cycle_list["EP2_LADDERMUL"]*255 + total_cycle_list["EP2_YRECOVER"]
                for operator in util_list["CONJ"].keys():
                    occupied_cycle = util_list["EP2_LADDERMUL"][operator]*255 + util_list["EP2_YRECOVER"][operator]
                    results_df.loc[operator] = occupied_cycle / total_cycle
                G2_results_df = pandas.concat([G2_results_df, results_df], axis=1)
                
                #  map to curve
                results_df = pandas.Series(index=util_list["CONJ"].keys(), name=config)
                total_cycle = total_cycle_list["2xSSWU_BEFORE_EXP"] + total_cycle_list["2xSSWU_AFTER_EXP"] + total_cycle_list["ISOGENY"] + total_cycle_list["EP_ADD_A_ANY"] + total_cycle_list["EP_ADD_A_0"]*6 + total_cycle_list["EP_DBL_A_0"]*63
                for operator in util_list["CONJ"].keys():
                    occupied_cycle = util_list["2xSSWU_BEFORE_EXP"][operator] + util_list["2xSSWU_AFTER_EXP"][operator] + util_list["ISOGENY"][operator] + util_list["EP_ADD_A_ANY"][operator] + util_list["EP_ADD_A_0"][operator]*6 + util_list["EP_DBL_A_0"][operator]*63
                    results_df.loc[operator] = occupied_cycle / total_cycle
                m2c_results_df = pandas.concat([m2c_results_df, results_df], axis=1)
                
                #  pairing (ML + FE)
                results_df = pandas.Series(index=util_list["CONJ"].keys(), name=config)
                total_cycle = total_cycle_list["EP2_DBL_w_EVAL"]*64 + total_cycle_list["EP2_ADD_w_EVAL"]*5 + total_cycle_list["SPARSE"]*68 + total_cycle_list["SQR"]*63 + total_cycle_list["MUL"]*37 + total_cycle_list["SQR012345"]*322 + total_cycle_list["CONJ"]*5 + total_cycle_list["FROB"]*8 + total_cycle_list["FP12_INV_BEFORE_FPINV"] + total_cycle_list["FP12_INV_AFTER_FPINV"]
                for operator in util_list["CONJ"].keys():
                    occupied_cycle = util_list["EP2_DBL_w_EVAL"][operator]*64 + util_list["EP2_ADD_w_EVAL"][operator]*5 + util_list["SPARSE"][operator]*68 + util_list["SQR"][operator]*63 + util_list["MUL"][operator]*37 + util_list["SQR012345"][operator]*322 + util_list["CONJ"][operator]*5 + util_list["FROB"][operator]*8 + util_list["FP12_INV_BEFORE_FPINV"][operator] + util_list["FP12_INV_AFTER_FPINV"][operator]
                    results_df.loc[operator] = occupied_cycle / total_cycle
                pairing_results_df = pandas.concat([pairing_results_df, results_df], axis=1)
                
                #  GT exp
                results_df = pandas.Series(index=util_list["CONJ"].keys(), name=config)
                total_cycle = total_cycle_list["FP12_LADDERMUL"]*255
                for operator in util_list["CONJ"].keys():
                    occupied_cycle = util_list["FP12_LADDERMUL"][operator]*255
                    results_df.loc[operator] = occupied_cycle / total_cycle
                GT_results_df = pandas.concat([GT_results_df, results_df], axis=1)
            except Exception as e:
                print(config, e)
    
    G1_results_df.to_csv("./whole_operation_hw_util.csv", mode="w")
    G2_results_df.to_csv("./whole_operation_hw_util.csv", mode="a", header=False)
    m2c_results_df.to_csv("./whole_operation_hw_util.csv", mode="a", header=False)
    pairing_results_df.to_csv("./whole_operation_hw_util.csv", mode="a", header=False)
    GT_results_df.to_csv("./whole_operation_hw_util.csv", mode="a", header=False)