# Two integers A and B are the inputs. Write a program to find GCD and LCM of A and B.

# Input
# The first line contains an integer T, total number of testcases. Then follow T lines, each line contains an integer A and B.

# Output
# Display the GCD and LCM of A and B separated by space respectively. The answer for each test case must be displayed in a new line.

def gcd(a, b):
  m = max(a, b)
  for j in range(m, 0, -1):
    if a%j == 0 and b%j == 0:
      return j
      break

def lcm(a, b):
  for k in range(1, (a*b)+1):
    if k%a == 0 and k%b == 0:
      return k
      break

t = int(input())
for i in range(t):
  l = [int(x) for x in input().split(" ")]
  a = l[0]
  b = l[1]
  print(gcd(a, b), lcm(a,b))
