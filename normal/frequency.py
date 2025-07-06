def iput():
    
    a = input("write something:\n")

    return a


def counter(a):

    count = {}

    for char in a:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1

    return count

text = iput ()
val =counter(text)
print ( val )


