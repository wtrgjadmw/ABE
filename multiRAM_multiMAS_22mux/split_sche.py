import copy, re
from formula_data import formulaData

# 大規模スケジューリングの分割

FIRST_DIVIDE = 20
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

    input_first = copy.deepcopy(inputs)
    knows = inputs
    # alls = []
    # alls += inputs
    # for s in formulas:
    #     alls.append(s[0])
    all_data += inputs
    cnt = 0
    split_ope: list[list[formulaData]] = [[] for i in range(0, 100)]
    split_index = 0
    divide_num = FIRST_DIVIDE  # RAMの読み出しのスケジューリングに時間がかかるので1番目だけ30, 後は70
    output_formulas = []
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
        else:
            split_ope[split_index] += split_tmp
        if cnt == 0:
            divide_num = BASIC_DIVIDE
            split_index += 1

        knows += knows_tmp
        cnt += 1
    print(knows)
    print(split_ope)
    if (set(knows) != set(all_data)):
        print("ng:split scheduling")
        exit()
    # split_ope内の[]を取り除く、冗長?
    split_ope_c: list[list[formulaData]] = []
    cnt = 0
    for s in split_ope:
        if s != []:
            split_ope_c.append(s)
            print(cnt, s)
            cnt += 1
    return split_ope_c, input_first, outputs, input_num
