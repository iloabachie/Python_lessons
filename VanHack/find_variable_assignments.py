
import ast
import builtins

def find_variable_assignments(source, target_var_names):
    tree = ast.parse(source)
    used_builtins = []
    # print(type(ast.walk(tree)))
    for node in ast.walk(tree):
        if isinstance(node, ast.arguments):
            for arg in node.args:
                if arg.arg in target_var_names:
                    # print(arg.arg)
                    used_builtins.append(arg.arg)
        if (isinstance(node, ast.FunctionDef) or isinstance(node, ast.ClassDef)) and node.name in target_var_names:
            if "__" == node.name[-2:]:
                pass
            else:
                used_builtins.append(node.name)
        if isinstance(node, ast.Assign):
            for target in node.targets:
                # print(target)
                if isinstance(target, ast.Tuple):
                    for elt in target.elts:
                        # print("8888", elt)
                        if isinstance(elt, ast.Name) and elt.id in target_var_names:
                            used_builtins.append(elt.id)   
                if isinstance(target, ast.Name) and target.id in target_var_names:
                    used_builtins.append(target.id)
                  
    # print("***", used_builtins)
    return list(set(used_builtins))


sources = [
"""
def fn():
    str = 42
    a, b = 1, 2
    print(str, a, b)
""", 
"""
def fn():
    "str = 42"
    '''next=42'''
    'bin = dir = next = list'
    next == 42
    a, b = str, list
    print(str, a, b)
""",
"""
def fn():
    next = 42
    str = next
    a, b = tuple, list
""",
"""
def fn(): 
    next,dir,list,dir = 1,2,3,"bin = 4"
str = 45
""",
"def reverse(str): return str[::-1]",
 """
def list(str, foo, iter): 
    def bin(set): 
        dict = 42 
        foo = zip
        bar = 0
    return str[::-1]
""",
"""
class str: 
    def __init__(self, list): 
        def next(foo, iter=42, baz=1): bin = 2
"""
]

if __name__ == "__main__":
    x=0
    for source in sources:
        print((x:=x+1), find_variable_assignments(source, dir(builtins)))
