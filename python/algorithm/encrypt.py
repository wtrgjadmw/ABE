import random
from parameter import p
from python.algorithm.att_tree import att_node, plc_tree

def calc_polynomial(polynomial: list[int], x: int):
    res = 0
    for i in range(len(polynomial)):
        res += polynomial[i] * (x ** i)
    return res

def generate_polynomial_matrix(plc_tree: att_node, parent_polynomial: list[int], is_root=False):
    if is_root:
        plc_tree.polynomial[0] = random.randint(0, p)
    else:
        plc_tree.polynomial[0] = calc_polynomial(parent_polynomial, plc_tree.index)
    for i in range(1, plc_tree.threshold_num):
        plc_tree.polynomial[i] = random.randint(0, p)
    print(plc_tree.index, plc_tree.polynomial)
    if plc_tree.children == None:
        return
    for child in plc_tree.children:
        generate_polynomial_matrix(child, plc_tree.polynomial)
        
if __name__ == "__main__":
    generate_polynomial_matrix(plc_tree, [], is_root=True)
    