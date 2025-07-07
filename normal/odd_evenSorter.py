

def iput():
    nums = input("Type some nums separated by spaces:\n")
    a = []
    for x in nums.split():
        a.append(int(x))
    
    return a

def sorter(a):

    even , odd = [] , []

    for num in a:
        if num % 2 == 0:
            even.append(num)
        else :
            odd.append(num)
    
    return even , odd 


val = iput()
even , odd = sorter(val)
print (f"""
    odd   =  {odd}
    even  =  {even}
""")




