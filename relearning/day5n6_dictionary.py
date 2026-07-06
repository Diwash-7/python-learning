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
        
def most_common_word(text):
    
    count = word_count(text)
    best_word = None
    best_count = 0
    for n in count:
        if count[n] > best_count:
            best_count = count[n]
            best_word = n

    return best_word
            
    

print(most_common_word("the cat sat on the mat the cat ran"))
