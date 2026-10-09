## converting normal expression (infix) into postfix expression using stacks

TOP = None

def isEmpty(stk):
    if stk == []:
        return True
        TOP = len(stk)
    else:
        return False

def push(stk, item):
    stk.append(item)
    TOP = len(stk) - 1

def pop(stk):
    if isEmpty(stk):
        print("Underflow")
        return None
    else:
        item = stk.pop()
        return item
        TOP = len(stk) - 1

def peek(stk):
    if isEmpty(stk):
        print("Underflow")
        return None
    else:
        TOP = len(stk) - 1
        return stk[TOP]

def size(stk):
    return len(stk)

def display(stk):
    if isEmpty(stk):
        print("Empty Stack")
    else:
        TOP = len(stk) - 1

        for x in range(TOP, -1, -1):
            print(stk[x])
