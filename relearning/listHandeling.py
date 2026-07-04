n= [1,2,3,10,20,33]

# Write a function that takes a list of numbers and returns the sum of only the even numbers.

def sum_even(n):
 
 total = 0

 for num in n:
  if num % 2 == 0:
   total =total +  num
 return total

print ( "sum of evens:",sum_even(n))

# Write a function that takes a list of numbers and returns a new list with only the odd numbers, in the same order.

def only_odd(n):

 odd = []

 for num in n:
  if num % 2 != 0:
   odd.append(num)
 
 return odd

print ("odd no.:",only_odd(n))

#Write a function that takes a string and returns how many vowels are in it.


def vowels(text):
  
  vowel=['a','e','i','o','u']
  count = 0
  
  for i in text:
    if i in vowel:
     count += 1
  
  return count

print ("no. of vowels:",vowels("khateee"))


#palindrom 

def is_palindrome(text):
  
  
  text=text.lower()
  
  return text == text[::-1]
  

print (is_palindrome("lloll"))


#Write a function that takes a sentence and returns it with the words in reverse order.

def reverse_words(text):
  
  words = text.split()
  
  return " ".join(words[::-1])

print (reverse_words("hello world how are you man "))