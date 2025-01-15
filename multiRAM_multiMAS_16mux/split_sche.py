import copy, re
from formula_data import formulaData

# 大規模スケジューリングの分割

FIRST_DIVIDE = 30
BASIC_DIVIDE = 50

def split_list(lst: list[formulaData], division_num: int):
    return [lst[i:i + division_num] for i in range(0, len(lst), division_num)]


def make_split_scheduling(formulas: list[formulaData]):
    inputs: list[str] = []
    outputs: list[str] = []
    input_num = 0
    all_data = []
    for s in formulas:
        all_data.append(s.result)
        outputs.append(s.result)
        for operand in s.operands:
            if operand in inputs:
                input_num += 1
            elif operand not in all_data:
                inputs.append(operand)
                input_num += 1
            if (operand in outputs) and (re.fullmatch(r"c[0-2]*", operand) is None):
                outputs.remove(operand)
    for s in formulas:
        if s.type == "CSEL":
            outputs += s.operands
            if s.result not in outputs:
                outputs.append(s.result)


    input_first = copy.deepcopy(inputs)
    knows = inputs
    all_data += inputs
    cnt = 0
    split_ope: list[list[formulaData]] = [[] for i in range(0, 100)]
    split_index = 0
    divide_num = FIRST_DIVIDE  # RAMの読み出しのスケジューリングに時間がかかるので1番目だけ30, 後は70
    while (set(knows) != set(all_data)):
        knows_tmp = []
        split_tmp: list[formulaData] = []

        for s in formulas:
            operand_is_calculated = True
            for operand in s.operands:
                if operand not in knows:
                    operand_is_calculated = False
            if operand_is_calculated & (s.result not in knows):
                knows_tmp.append(s.result)
                split_tmp.append(s)

        if len(split_ope[split_index]) + len(split_tmp) > divide_num:
            divided_split_tmp = split_list(split_tmp, divide_num)
            for i in range(len(divided_split_tmp)):
                if len(split_ope[split_index]) != 0:
                    split_index += 1
                split_ope[split_index] += divided_split_tmp[i]
            if split_index != 0:
                divide_num = BASIC_DIVIDE

        else:
            split_ope[split_index] += split_tmp
        # if cnt == 0:
        #     divide_num = BASIC_DIVIDE
        #     split_index += 1

        knows += knows_tmp
        # cnt += 1
    # print(knows)
    # print(split_ope)
    if (set(knows) != set(all_data)):
        print("ng:split scheduling")
        exit()
    # split_ope内の[]を取り除く、冗長?
    split_ope_c: list[list[formulaData]] = []
    cnt = 0
    for s in split_ope:
        if s != []:
            split_ope_c.append(s)
            # print(cnt, s)
            cnt += 1
    
    # 2xSSWU_BEFORE_EXP
    # input_first = ['t0', 't1', 'A_', 'ONE', 'B_', 'negA_', 'xi', 'xiA', 'Z_Hash0', 'Z_Hash1', 'D0', 'D1']
    # outputs = ['UV30', 'UV31', 'Z_Hash0', 'Z_Hash1', 'UV0', 'UV1', 'V0', 'V1', 'D0', 'D1', 'U0', 'U1', 'N0', 'N1', 't20', 't21', 'xit20', 'xit21']   
    # 2xSSWU_AFTER_EXP
    input_first = ['UV3_exp0', 'UV0', 'UV3_exp1', 'UV1', 'Z_Hash0', 'Z_Hash1', 'V0', 'V1', 'xit20', 'N0', 'xit21', 'N1', 't20', 't0', 't21', 't1', 'sqrt_negxi3', 'U0', 'U1', 'ZERO', 'alpha2V_U0', 'alpha2V_U1', 'xit2N0', 'xit2N1', 'y0', 'y1', 'alpha0', 'alpha1', 'y20', 'y21', 'y_alt0', 'y_alt1', 'ONE', 'Y_0', 'Y_1']
    outputs = ['X_Hash0', 'X_Hash1', 'Y_Hash0', 'Y_Hash1', 'xit2N0', 'xit2N1', 'alpha2V_U0', 'y20', 'alpha2V_U1', 'y21', 'y0', 'y_alt0', 'y1', 'y_alt1', 'Y_0', 'Y_1', 'alpha0', 'alpha1'] 
    return split_ope_c, input_first, outputs, input_num
