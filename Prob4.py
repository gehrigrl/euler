#this code assumes the answer is above 249001=499*499
#the decimals generated in quotients (999.0 vs 999) messed up my code 
import math
def is_palindrome(n):
 n=str(n)
 for i in range(math.floor(len(n))):
  if n[i] != n[(len(n)-1)-i]:
    return False 
 return True   
     
def is_pair(n):
 for i in range(500):
    if n % (999-i) == 0:
      if len(str(n//(999-i))) == 3:
        a=n/(999-i)
        b=(999-i)
        return(a,b)
 return False
 
for i in range(400000):
  if is_palindrome(998001-i):
   if is_pair(998001-i):
    print(998001-i)
    break
