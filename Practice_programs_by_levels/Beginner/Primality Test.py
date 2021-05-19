# Alice and Bob are meeting after a long time. As usual they love to play some math games. This times Alice takes the call and decides the game. The game is very simple, Alice says out an integer and Bob has to say whether the number is prime or not. Bob as usual knows the logic but since Alice doesn't give Bob much time to think, so Bob decides to write a computer program.
# Help Bob accomplish this task by writing a computer program which will calculate whether the number is prime or not .

# Input
# The first line of the input contains an integer T, the number of testcases. T lines follow.
# Each of the next T lines contains an integer N which has to be tested for primality.

# Output
# For each test case output in a separate line, "yes" if the number is prime else "no."

t = int(input())
for i in range(t):
  num = int(input())
  count = 0
  for j in range(1, num+1):
    if num % j == 0:
      count += 1
  if count == 2:
    print("yes")
  else:
    print("no")
