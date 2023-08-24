import sys
import operator


def main():
    """Implement the calculator"""
    left_operand = int(sys.argv[1])
    op_name = sys.argv[2]
    right_operand = int(sys.argv[3])
    if op_name == '+':
        return left_operand + right_operand
    if op_name == '-':
        return left_operand - right_operand
    if op_name == '*':
        return left_operand * right_operand
    if op_name == '/':
        return left_operand / right_operand
    return 'usage: '

def main2():
    ops = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y,
    }
    return ops[sys.argv[2]](int(sys.argv[1]), int(sys.argv[3]))

def main3():
    return {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }[sys.argv[2]](int(sys.argv[1]), int(sys.argv[3]))

def main4():
    #getattr(1,'__add__',2)
    return getattr(int(sys.argv[1]), {
        '+': '__add__',
        '-': '__sub__',
        '*': '__mul__',
        '/': '__truediv__'
    }[sys.argv[2]])(int(sys.argv[3]))

def main5():
    return eval(f'{sys.argv[1]} {sys.argv[2]} {sys.argv[3]}')

if __name__ == "__main__":
    print(main())
    
    # print(main2())
    # print(main3())
    # print(main4())
    # print(main5())
    
