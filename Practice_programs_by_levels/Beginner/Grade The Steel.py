# A certain type of steel is graded according to the following conditions.
# Hardness of the steel must be greater than 50
# Carbon content of the steel must be less than 0.7
# Tensile strength must be greater than 5600
# The grades awarded are as follows:
# Grade is 10 if all three conditions are met
# Grade is 9 if conditions (1) and (2) are met
# Grade is 8 if conditions (2) and (3) are met
# Grade is 7 if conditions (1) and (3) are met
# Grade is 6 if only one condition is met
# Grade is 5 if none of the three conditions are met
# Write a program to display the grade of the steel, based on the values of hardness, carbon content and tensile strength of the steel, given by the user.

# Input
# The first line contains an integer T, total number of testcases. Then follow T lines, each line contains three numbers hardness, carbon content and tensile strength of the steel.

# Output
# For each test case, print Grade of the steel depending on Conditions, in a new line.

t = int(input())
for i in range(t):
  l = [float(x) for x in input().split(" ")]
  h = l[0]
  c = l[1]
  t = l[2]
  con = []
  if h > 50:
    con.append(1)
  if c > 0.7:
    con.append(2)
  if t > 5600:
    con.append(3)
  if 1 and 2 and 3 in con:
    print(10)
  elif 1 and 2 in con:
    print(9)
  elif 2 and 3 in con:
    print(8)
  elif 1 and 3 in con:
    print(7)
  elif 1 or 2 or 3 in con:
    print(6)
  else:
    print(5)
