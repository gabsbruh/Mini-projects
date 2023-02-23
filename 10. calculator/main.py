# calculator project with inputs like
# +
# -
# *
# /
# ^
# !
# & which means sqrt

operations = {} # types of operations in 1 dictionary

def add(a, b):
    return a + b

def substract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def exponent(a, b):
    return a**b

def factorial(n):
   if n == 1:
       return n
   else:
       return n*factorial(n-1)

def root(a, x):
    """calculating root with given degree

    Args:
        a (float): number to root
        x (int): degree
    """
    return a**(1/x)

operations = {
    "+" : add,
    "-" : substract,
    "*" : multiply,
    "/" : divide,
    "^" : exponent,
    "!" : factorial,
    "&" : root
}

def calculate():
    """Function to choose the operation and depends on number of variables and operation calculate it

    Returns:
        float: calculated number
    """
    print("Which operation would you like to do ?")
    for opr in operations:
        print(opr + " - " +  str(operations[opr])[10:14])
    op = input("My operation: ")
    if op == "!":
        n = float(input(" Choose your number: "))
        return (operations[op](n))
    elif op == "&":
        a = float(input("choose a number to root: "))
        x = float(input("choose the degreee of rooting: "))
        return (operations[op](a, x))
    elif op in operations:
        a = float(input(f"choose a first number: "))
        b = float(input(f"choose a second number: "))
        return (operations[op](a, b))
    else:
        print("Wrong input!")
        calculate()

def looping_calculate(function):
    """function that using function and making it loop as many times as user wants to.
    """
    is_cont = True  
    while is_cont:
        is_cont = False
        print(function)
        is_continue = input(f"Would you like to try again? Type 'yes' or 'no'\n")
        if is_continue == 'yes':
            is_cont = True
        elif is_continue == 'no':
            print("Goodbye!")
            break    
        else:
            print("Wrong input!")
            is_continue = True

# RUN 
M = 0 # memory of calculator
looping_calculate(calculate())

