

#################################
##  i knoow this code sucks !! ##
#################################
    
a = []

for  i in range(5) :
    val = int(input("enter numbers:\n"))
    a.append(val)

b = None

def main (a,b):
    for j in range(4) :
        for i in range(4) :
            if a[i] < a[i+1] :
                 b=a[i]
                 a[i] = a[i+1]
                 a[i+1] = b

    return a

r = main (a,b)
print (r)
print (r[0])
print (r[4])
 

print (int(sum(a)/len(a)))





    
    