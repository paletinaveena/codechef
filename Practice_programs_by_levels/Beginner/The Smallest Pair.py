# You are given a sequence a1, a2, ..., aN. Find the smallest possible value of ai + aj, where 1 ≤ i < j ≤ N.

# Input
# The first line of the input contains an integer T denoting the number of test cases. The description of T test cases follows.
# The first line of each description consists of a single integer N.
# The second line of each description contains N space separated integers - a1, a2, ..., aN respectively.

# Output
# For each test case, output a single line containing a single integer - the smallest possible sum for the corresponding test case.

t = int(input())
for i in range(t):
  n = int(input())
  l = [int(x) for x in input().split(" ")]
  l.sort()
  print(l[0]+l[1])
