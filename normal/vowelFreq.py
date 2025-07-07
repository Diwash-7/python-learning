
def iput():

    a = []
    a = input ("Type something : \n")

    return a

def vowel_freq(a):

    count = 0     

    vowel = ['a','e','i','o','u']

    for char in a:
        if char.lower() in vowel:
            count += 1
    
    return count 

text = iput()
no_of_vowels = vowel_freq(text)
percent = (no_of_vowels/len(text))*100
print(f"No. of vowels = {no_of_vowels}")
print(f"total letters = {len(text)}")
print (f"% of vowel = {percent:.2f}%")


    

