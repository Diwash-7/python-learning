def sum(a,b):
    return a+b
def sub(a,b):
    return a-b
def product(a,b):
    return a*b
def divide(a,b):
    return a/b

a=float(input("a:"))
b=float(input("b:"))

choose=input("choose:\n1=+\t2=-\n3=*\t4=/\n")

if choose=="1":
    print(sum(a,b))
elif choose=="2":
    print(sub(a,b))
elif choose=="3":
    print(product(a,b))
elif choose=="4":
    print(divide(a,b))
else:
    print("invalid")