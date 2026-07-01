# Write a function that takes a list of numbers and returns the sum of only the even numbers.

n= [1,2,3,10,20,34]

def sum(n):
 
 total = 0

 for num in n:
  if num % 2 == 0:
   total =total +  num
 return total

print (sum(n))

