jd=0.000000000000001
x=1
y=int(input("please input a number: "))
n=1
while n>jd:
    x=(y/x+x)/2
    n=abs(y-x*x)
print(x)