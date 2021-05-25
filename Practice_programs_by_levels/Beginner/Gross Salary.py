# In a company an emplopyee is paid as under: If his basic salary is less than Rs. 1500, then HRA = 10% of base salary and DA = 90% of basic salary. If his salary is either equal to or above Rs. 1500, then HRA = Rs. 500 and DA = 98% of basic salary. If the Employee's salary is input, write a program to find his gross salary.
# NOTE: Gross Salary = Basic Salary + HRA + DA

# Input
# The first line contains an integer T, total number of testcases. Then follow T lines, each line contains an integer salary.

# Output
# For each test case, output the gross salary of the employee in a new line. Your answer will be considered correct if the absolute error is less than 10-2.

t = int(input())
for i in range(t):
  n = int(input())
  if n < 1500:
    hra = n/10
    da = (n * 9) / 10
  else:
    hra = 500
    da = (n * 98) / 100
  gs = n + hra + da
  print(f"{gs:.2f}")