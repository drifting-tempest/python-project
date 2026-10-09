## converting normal expression (infix) into postfix expression using stacks

TOP = None
def isEmpty(stk):

    if stk == []:

        global TOP
        TOP = len(stk)
        return True 
    else:
        return False

def push(stk, item):

    stk.append(item)

    global TOP
    TOP = len(stk) - 1

def pop(stk):

    if isEmpty(stk):
        print("Underflow")
        return None
    
    else:
        item = stk.pop()
        global TOP

        TOP = len(stk) - 1
        return item

def peek(stk):

    if isEmpty(stk):
        print("Underflow")
        return None
    
    else:
        global TOP
        TOP = len(stk) - 1
        return stk[TOP]

def size(stk):
    return len(stk)

def display(stk):
    if isEmpty(stk):
        print("Empty Stack")
    else:

        global TOP
        TOP = len(stk) - 1

        for x in range(TOP, -1, -1):
            print(stk[x])


## postfix to infix 

# finding the priority of an operator
def preced(op):
    if op == '+' or op == '-':
        return 1
    elif op == '*' or op == '/':
        return 2
    else:
        return 0

def infix_to_postfix(expression):
    stk = []            
    postfix = ""         
    tokens = expression.split()

    for i in range(len(tokens)):
        token = tokens[i]

        if token.isdigit():
            postfix = postfix + token + " "

        elif token == "(":
            push(stk, token)

        elif token == ")":
            while peek(stk) != "(":
                x = pop(stk)
                postfix = postfix + x + " "
            pop(stk)      

        else:
            while isEmpty(stk) == False and peek(stk) != "(" and preced(peek(stk)) >= preced(token):
                x = pop(stk)
                postfix = postfix + x + " "
            push(stk, token)

    while isEmpty(stk) == False:
        x = pop(stk)
        postfix = postfix + x + " "

    postfix_final = postfix.strip()

    return postfix_final

##solving postfix expression

def evaluate_postfix(expression):
    stk = []         
    tokens = expression.split()

    for i in range(len(tokens)):
        token = tokens[i]

        if token.isdigit():
            num = int(token)
            push(stk, num)

        else:
            num2 = pop(stk)   
            num1 = pop(stk)   

            if token == '+':
                result = num1 + num2
            elif token == '-':
                result = num1 - num2
            elif token == '*':
                result = num1 * num2
            elif token == '/':
                result = num1 / num2

            push(stk, result)

    answer = pop(stk)
    return answer


##final part of program

infix = input("ENter the infix expression you would like to evaluate: ")

postfix = infix_to_postfix(infix)
print("Postfix expression:", postfix)

answer = evaluate_postfix(postfix)
print("Result:", answer)