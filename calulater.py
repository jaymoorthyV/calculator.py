def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mult(a,b):
    return a*b

def division(a,b):
    return a/b

opretor ={'+':add,'-':sub,'*':mult,'/':division}

num1=float(input('enter a first number:'))
should_continue=False
while not should_continue:
    for keys in opretor:
        print(keys)
    opertion=input('please select a operation:')

    num2=float(input('enter next number:'))
    calculation=opretor[opertion]
    c1=calculation(num1,num2)
    print(f"{num1}{opertion}{num2}={c1}")

    con=input(f"do you want to contineus calculation with{c1}")

    if con=='no':
            should_continue=True
    else:
            num1=c1
