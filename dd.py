def mult(times):
  OK=0
  while OK<times:
   a=input("please input a number: ")
   b=input("please input another number: ")
   c=int(a)*int(b)
   d=int(input("please input the product: "))
   if d==c:
  	 OK+=1
if __name__=="__main__":
 mult(2)