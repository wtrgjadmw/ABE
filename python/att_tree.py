
import re

class att_node:
    def __init__(self, att: str, index: int, threshold_num: int, children = None) -> None:
        self.att = att
        self.index = index
        self.threshold_num = threshold_num
        self.children = children
        

def split_policy_str(plc_str: str):
    tokens = re.findall(r'\w+|\&|\||\(|\)', plc_str)
    output = []
    operators = []
    
    for token in tokens:
        if token == '&' or token == '|':
            operators.append(token)
        elif token == '(':
            operators.append(token)
        elif token == ')':
            while operators and operators[-1] != '(':
                output.append(operators.pop())
            operators.pop()
        else:
            output.append(token)
    
    while operators:
        output.append(operators.pop())
    
    return output

def generate_policy_tree(plc_str: str):
    rpn = split_policy_str(plc_str)
    stack = []
    index = 0
    for token in rpn:
        if token == '&':
            b = stack.pop()
            a = stack.pop()
            new_tree = att_node(att="", index=index, threshold_num=2, children=[a, b])
            index += 1
            stack.append(new_tree)
        elif token == '|':
            b = stack.pop()
            a = stack.pop()
            new_tree = att_node(att="", index=index, threshold_num=1, children=[a, b])
            index += 1
            stack.append(new_tree)
        else:
            new_node = att_node(att=token, index=index, threshold_num=1, children=None)
            index += 1
            stack.append(new_node)
    return stack[0]

def check_plc_sat(plc_tree:att_node, att_list:list[str]) -> bool:
    if plc_tree.children == None:
        result = (plc_tree.att in att_list)
        print("{} is{} satisfied".format(plc_tree.att, "" if result else " not") )
        return result
    cnt = 0
    for child in plc_tree.children:
        if check_plc_sat(child, att_list):
            cnt += 1
    return cnt >= plc_tree.threshold_num

policy = "A | ((B & C) | D)"
plc_tree = generate_policy_tree(policy)
att_list1 = ['A']
att_list2 = ['B']
att_list3 = ['B', 'C']
print(check_plc_sat(plc_tree, att_list1))
print(check_plc_sat(plc_tree, att_list2))
print(check_plc_sat(plc_tree, att_list3))
