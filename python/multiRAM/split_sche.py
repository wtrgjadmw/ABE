import copy, re
# 大規模スケジューリングの分割


def split_list(lst, division_num):
    return [lst[i:i + division_num] for i in range(0, len(lst), division_num)]


def make_split_scheduling(formulas):
    inputs = []
    outputs = []
    input_num = 0
    d = []
    for s in formulas:
        d.append(s[0])
        outputs.append(s[0])
        if s[2] in inputs:
            input_num += 1
        elif s[2] not in d:
            inputs.append(s[2])
            input_num += 1
        if s[3] in inputs:
            input_num += 1
        elif s[3] not in d:
            inputs.append(s[3])
            input_num += 1
        if s[2] in outputs:
            outputs.remove(s[2])
        if s[3] in outputs:
            outputs.remove(s[3])
    input_first = copy.deepcopy(inputs)
    knows = inputs
    alls = []
    alls += inputs
    for s in formulas:
        alls.append(s[0])
    split_ope = [[] for i in range(0, 100)]
    split_index = 0
    DIVIDE_NUM = 30  # RAMの読み出しのスケジューリングに時間がかかるので1番目だけ30, 後は70
    add_num = 0
    mul_num = 0
    output_formulas = []
    while (set(knows) != set(alls)):
        knows_tmp = []
        split_tmp = []

        for s in formulas:
            # "square", "mulFp2"などは一般性欠く
            if (s[2] in knows) and (s[3] in knows):
                if (s[0] not in knows):
                    knows_tmp.append(s[0])
                    if s[0] in outputs:
                        output_formulas.append(s)
                    else:
                        split_tmp.append(s)
                        if s[1] == "MUL":
                            mul_num += 1
                        elif s[1] == "ADD" or s[1] == "SUB":
                            add_num += 1

        if len(split_ope[split_index]) + len(split_tmp) > DIVIDE_NUM:
            divided_split_tmp = split_list(split_tmp, DIVIDE_NUM)
            for i in range(len(divided_split_tmp)):
                if len(split_ope[split_index]) != 0:
                    split_index += 1
                split_ope[split_index] += divided_split_tmp[i]
            if DIVIDE_NUM == 30:
                DIVIDE_NUM = 70
                split_index += 1
        else:
            split_ope[split_index] += split_tmp

        knows += knows_tmp
    if (set(knows) != set(alls)):
        print("ng:split scheduling")
        exit()
    # split_ope内の[]を取り除く、冗長?
    split_ope_c = []
    for s in split_ope:
        if s != []:
            split_ope_c.append(s)
    if len(split_ope_c) == 0:
        split_ope_c = [output_formulas]
    else:
        split_ope_c[-1] += output_formulas
    print(split_ope_c)
    return split_ope_c, input_first, outputs, input_num
