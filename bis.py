def bis(l,x):
  lw=0
  hg=len(l)-1
  while lw<=hg:
    i=(lw+hg)//2 
    if l[i]>x:
      hg=i-1
    elif l[i]<x:
      lw=i+1
    elif l[i]==x:
      return i
  return "a-oh,it's not inside the list"
a=[11,12,13,14,15]
print(bis(a,16))