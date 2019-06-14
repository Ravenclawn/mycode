i=1
while i<10:
  for j in range (i,10):
    print("%d*%d=%2d" %(i,j,i*j), end=' ')
  print('')
  print("       "*i, end='')
  i+=1