list=[1,2,3]
sum=2
while (list[1]+list[2])<4000000:
 list[0]=list[1]
 list[1]=list[2]
 list[2]=list[0]+list[1]
 if list[2] % 2 == 0:
   sum += list[2]
print(sum)

