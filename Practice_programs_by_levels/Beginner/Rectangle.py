# You are given four integers a, b, c and d. Determine if there's a rectangle such that the lengths of its sides are a, b, c and d (in any order).

# Input
# The first line of the input contains a single integer T denoting the number of test cases.
# The description of T test cases follows.
# The first and only line of each test case contains four space-separated integers a, b, c and d.

# Output
# For each test case, print a single line containing one string "YES" or "NO".

t = int(input())
for i in range(t):
  l = [int(x) for x in input().split(" ")]
  l.sort()
  if l[0]==l[1] and l[2]==l[3]:
    print("YES")
  else:
    print("NO")
