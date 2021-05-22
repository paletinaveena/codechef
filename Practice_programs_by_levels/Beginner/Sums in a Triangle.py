# Let's consider a triangle of numbers in which a number appears in the first line, two numbers appear in the second line, three in the third line, etc. 
# Develop a program which will compute the largest of the sums of numbers that appear on the paths starting from the top towards the base, so that:
# on each path the next number is located on the row below, more precisely either directly below or below and one place to the right; the number of rows is strictly positive, but less than 100 all numbers are positive integers between 0 and 99.

# Input
# In the first line integer n - the number of test cases (equal to about 1000). Then n test cases follow. Each test case starts with the number of lines which is followed by their content.

# Output
# For each test case write the determined value in a separate line.

# Method - 1
t = int(input())
for i in range(t):
  n = int(input())
  total = 0
  for j in range(n):
    l = [int(x) for x in input().split(" ")]
    for num in l:
      total += num
  print(total//2)

  # Method - 2
  for _ in range(int(input())):
    n=int(input())
    ar=[]
    for i in range(n):
        l=list(map(int, input().split()))[:i + 1]
        ar.append(l)
    for j in range(n - 1, 0, -1):
        for k in range(0, j):
            if ar[j][k] > ar[j][k + 1]:
                ar[j - 1][k] = ar[j - 1][k] + ar[j][k]
            else:
                ar[j - 1][k] = ar[j - 1][k] + ar[j][k + 1]
    print(ar[0][0])
