def iput():
    
    a = input("write something:\n")

    return a


def counter(a):

    count = {}
    words = a.split()

    for c in words :
        if c in count:
            count[c]+= 1
        else :
            count[c] = 1

    return count

text = input()
ans = counter(text)

print(ans)  

max_v = max(ans.values())

for word in ans :
   if ans[word] == max_v :
       print ( f"{word}:{ans[word]}")
