def iput():
    
    a = input("write something:\n")

    return a


def bad_word(a):

    bad = ['fuck','shit','noob' ]
    censor = False
    words = a.split()

    for i in range (len(words)):
        if words[i].lower() in bad:
            star = '*'*len(words[i])
            words[i]=star
            censor = True
 
    censored_text = ' '.join(words)
    # censored_text =  words
    return censor , censored_text
    


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

warn , val = bad_word(text)

print (val)
if warn:
    print("watch your language !!!")