# Chefina loves cakes! N suitors numbered 1…N have arrived from across the seven seas to woo her.

# Each of the suitors wishes to impress Chefina, so suitor i has prepared a cake of height Hi. To test the suitors, Chefina assigned them Q tasks. Each of the tasks is of one of the following types:

# 1 L R X: Increase the heights of all cakes in the range L to R inclusive by X, i.e., increase each of HL, HL+1, HL+2… HR by X.

# 2: Find the sum of heights of all cakes prepared by odd-numbered suitors.

# 3: Find the sum of heights of all cakes prepared by even-numbered suitors.
# Can you help the suitors complete the tasks?

# Input:

# The first line contains an integer N, the number of cakes.

# The next line contains N space-separated integers H1,H2,…,HN, denoting the heights of the cakes.

# The third line contains an integer Q, the number of tasks.

# The next Q lines describe the tasks assigned to the suitors by Chefina.

# Output:

# For each task of type 2 or 3, display the sum of heights of all cakes prepared by odd or even-numbered suitors, respectively, on a new line.


def fun(operation):
    global evenc
    global oddc
    total  = operation[2]-operation[1]+1
    N = (operation[2]-operation[1])//2
    odd=even=0
    if(operation[2] % 2 != 0 or operation[1] % 2 != 0):
        N += 1
    odd=N
    even = total-N
    evenc += (operation[3]*even)
    oddc+=  (operation[3]*odd)
    return 0



def fun2():
    global evenc
    global oddc
    evenc=oddc=0
    for i in range (0,n):
        if(i%2==0):
            oddc+= cakes[i]
        else:
            evenc+= cakes[i]
    return evenc,oddc


n = int(input())
cakes = list(map(int,input().split()))
no_of_operation = int(input())
evenc,oddc = fun2()

for i in range(0,no_of_operation):
    operation = list(map(int,input().split()))
    if operation[0]==1:
        fun(operation)
    elif operation[0]==2:
        print(oddc)
    else:
        print(evenc)
