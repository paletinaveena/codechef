
# Chef Two and Chef Ten are playing a game with a number X. In one turn, they can multiply X by 2. The goal of the game is to make X divisible by 10.
# Help the Chefs find the smallest number of turns necessary to win the game (it may be possible to win in zero turns) or determine that it is impossible.

# Input
# The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
# The first and only line of each test case contains a single integer denoting the initial value of X.

# Output
# For each test case, print a single line containing one integer — the minimum required number of turns or −1 if there is no way to win the game.

t = int(input())
for i in range(t):
  n = int(input())
  for j in range(10):
    if n%10 == 0:
      print(j)
      break
    else:
      n *= 2
  else:
    print(-1)
