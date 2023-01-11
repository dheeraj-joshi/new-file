def fact(n):
    if n==1:
       return 1 
    else:
       return  n *fact(n-1)
n=int (input("enter the interger value: ")) 
a=fact(n)
print(a)
#find the fiboonaci series by using recurrsion
def fibo(n):
    if n<=1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
n=int(input("enter the integer:"))
if n<=0:
    print("enter a valid integer:")
else:
    for i in range(0,n):
        print(fibo(i))
        





