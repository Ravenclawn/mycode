def func(l):
 a=len(l)
 while a>0:
   for i in range(0,a-1):
     if l[i]>l[i+1]:
       l[i],l[i+1]=l[i+1],l[i]
   a-=1
 print(l)
l=[2,8,6,7,7]
print(func(l))


#3 = input()
#print(print(int(s3)))