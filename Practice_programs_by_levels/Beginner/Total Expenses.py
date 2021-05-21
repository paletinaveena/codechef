# While purchasing certain items, a discount of 10% is offered if the quantity purchased is more than 1000. If the quantity and price per item are input, write a program to calculate the total expenses.

# Input
# The first line contains an integer T, total number of test cases. Then follow T lines, each line contains integers quantity and price.

# Output
# For each test case, output the total expenses while purchasing items, in a new line.

t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    if a>1000:
        pr=0.9*(a*b)
        print (pr)
    else:
        pr=(a*b)
        print (pr)
