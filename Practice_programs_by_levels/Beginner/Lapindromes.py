# Lapindrome is defined as a string which when split in the middle, gives two halves having the same characters and same frequency of each character.
# If there are odd number of characters in the string, we ignore the middle character and check for lapindrome.
# For example gaga is a lapindrome, since the two halves ga and ga have the same characters with same frequency.
# Also, abccab, rotor and xyzxy are a few examples of lapindromes. Note that abbaab is NOT a lapindrome.
# The two halves contain the same characters but their frequencies do not match.
# Your task is simple. Given a string, you need to tell if it is a lapindrome.

# Input:
# First line of input contains a single integer T, the number of test cases.
# Each test is a single line containing a string S composed of only lowercase English alphabet.

# Output:
# For each test case, output on a separate line: "YES" if the string is a lapindrome and "NO" if it is not.

t = int(input())
for i in range(t):
  n = input()
  c = len(n)
  f_l = []
  b_l = [] 
  if c%2 == 0:
    for j in range(0, (c//2)):
      f_l.append(n[j])
    for k in range((c//2), c):
      b_l.append(n[k]) 
  else:
    for j in range(0, (c//2)):
      f_l.append(n[j])
    for k in range((c//2)+1, c):
      b_l.append(n[k])  
  a = 0
  for l in range(len(f_l)):
      for i in f_l:
          if i in b_l:
              a += 1
              f_l.remove(i)
              b_l.remove(i)
  if a == (c//2):
    print("YES")
  else:
    print("NO")
