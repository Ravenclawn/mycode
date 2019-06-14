count2=0
count=1
print("prime between 1--1000: ")
while count<2:
 for loop in range(2,1000):
  j=int(loop**0.5)
  while loop % j !=0:
  	j-=1
  if j==1:
       print("%3d " %loop, end='')
       count2+=1
       if count2 % 16==0:
         print('')
 count+=1
print(end='\n')
print("total number: "+str(count2))