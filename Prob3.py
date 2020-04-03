import math
def min_factor(n):
  for i in range(2,int(math.ceil(n/2))):
    if n % i == 0:
      return i   
  return 1     
top=75143
while min_factor(top) > 1:
 top=top//min_factor(top)
print(top)

#could retry with a recursive function
#could retry with range having a new minimum value each iteration
