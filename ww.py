def bubble(l):
	i=len(l)
	while i>0:
	  for j in range(0,i-1):
		  if l[j]>l[j+1]:
			  l[j],l[j+1]=l[j+1],l[j]
			  print(l)

	  i=i-1
	print(l)
a=[8,7,6,5,4,3,2,1]
bubble(a)