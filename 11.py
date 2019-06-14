f=open("hyke.txt","r")
texts=f.read()
f.close()
a=[]
for ch in texts:
  a.append(ch)
#print(a)
D1={}
D2={}
for ch in a:
  m=ord(ch)
  if m>=19968 and m<=40869:
           if ch in D1:
             D1[ch]+=1
           else:
             D1[ch]=1
  else:
      if ch in D1:
        D2[ch]+=1
      else:
        D2[ch]=1
print(D1)
print(len(D1))