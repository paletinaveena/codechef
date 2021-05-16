# Consider a currency system in which there are notes of six denominations, namely, Rs. 1, Rs. 2, Rs. 5, Rs. 10, Rs. 50, Rs. 100. 
# If the sum of Rs. N is input, write a program to computer smallest number of notes that will combine to give Rs. N.

# Input
# The first line contains an integer T, total number of testcases. Then follow T lines, each line contains an integer N.

# Output
# For each test case, display the smallest number of notes that will combine to give N, in a new line.

n = int(input())
for i in range(n):
   p = int(input())
   l = [100,50,10,5,2,1]
   x = 0
   for i in l:
      x = x+(p//i)
      p = p % i
   print(x)    
