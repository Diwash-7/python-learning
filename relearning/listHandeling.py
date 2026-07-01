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
