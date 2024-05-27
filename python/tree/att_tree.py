
import re

class att_node:
    def __init__(self, att, children = None) -> None:
        self.att = att
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
    for token in rpn:
        if token == '&' or token == '|':
            b = stack.pop()
            a = stack.pop()
            new_tree = att_node(att=token, children=[a, b])
            stack.append(new_tree)
        else:
            new_node = att_node(att=token, children=None)
            stack.append(new_node)
    return stack[0]

def check_plc_sat(plc_tree:att_node, att_list:list[str]) -> bool:
    if plc_tree.children == None:
        result = (plc_tree.att in att_list)
        print("{} is{} satisfied".format(plc_tree.att, "" if result else " not") )
        return result
    a = plc_tree.children[0]
    b = plc_tree.children[1]
    if plc_tree.att == '&':
        is_satisfied = check_plc_sat(a, att_list) & check_plc_sat(b, att_list)
    elif plc_tree.att == '|':
        is_satisfied = check_plc_sat(a, att_list) | check_plc_sat(b, att_list)
    return is_satisfied

policy = "A | ((B & C) | D)"
plc_tree = generate_policy_tree(policy)
att_list1 = ['A']
att_list2 = ['B']
att_list3 = ['B', 'C']
print(check_plc_sat(plc_tree, att_list1))
print(check_plc_sat(plc_tree, att_list2))
print(check_plc_sat(plc_tree, att_list3))
