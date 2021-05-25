# The chef has a recipe he wishes to use for his guests, but the recipe will make far more food than he can serve to the guests.
# The chef therefore would like to make a reduced version of the recipe which has the same ratios of ingredients, but makes less food.
# The chef, however, does not like fractions.
# The original recipe contains only whole numbers of ingredients, and the chef wants the reduced recipe to only contain whole numbers of ingredients as well.
# Help the chef determine how much of each ingredient to use in order to make as little food as possible.

# Input
# Input will begin with an integer T, the number of test cases. Each test case consists of a single line.
# The line begins with a positive integer N, the number of ingredients. N integers follow, each indicating the quantity of a particular ingredient that is used.

# Output
# For each test case, output exactly N space-separated integers on a line, giving the quantity of each ingredient that 
# the chef should use in order to make as little food as possible.

t = int(input())
for i in range(t):
  l = [int(x) for x in input().split(" ")]
  lis = []
  for j in range(1,l[0]+1):
    lis.append(l[j])
  m = min(lis)
  for k in range(m,0,-1):
    count = 0
    for char in lis:
      if char % k == 0:
        count += 1
    if count == len(lis):
      break
  ans = []
  for char in lis:
    a = char//k
    ans.append(str(a))
  print(" ".join(ans))
