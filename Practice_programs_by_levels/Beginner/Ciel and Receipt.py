# Tomya is a girl. She loves Chef Ciel very much.
# Tomya like a positive integer p, and now she wants to get a receipt of Ciel's restaurant whose total price is exactly p. 
# The current menus of Ciel's restaurant are shown the following table.
# Note that the i-th menu has the price 2i-1 (1 ≤ i ≤ 12).
# Since Tomya is a pretty girl, she cannot eat a lot. So please find the minimum number of menus whose total price is exactly p. Note that if she orders the same menu twice, then it is considered as two menus are ordered. (See Explanations for details)

# Input
# The first line contains an integer T, the number of test cases. Then T test cases follow. Each test case contains an integer p.

# Output
# For each test case, print the minimum number of menus whose total price is exactly p.

t=int(input())
for i in range(t):
    l=[2048,1024,512,256,128,64,32,16,8,4,2,1]
    a=0
    n=int(input())
    while n>0:
        for i in l:
            if(i<=n):
                a=a+(n//i)
                n=n%i 
    print(a)
