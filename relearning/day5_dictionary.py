#program that takes a string and returns a dictionary mapping each word to how many times it appears. Case-insensitive

def word_count(text):
    count = {}
    words = text.lower().split()
    
    for word in words:
        if word in count:
            count[word] += 1
        else :
            count[word] = 1
    
    
    return count

print (word_count("what the hell is this man what ?"))  
        