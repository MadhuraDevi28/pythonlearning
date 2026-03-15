#write a program to 1. get a input using a function
#2. get a input & check that number is divisible by 5 if yes then print "yes" or "no"
#3. Get 2 input & iterate them & sum them both iterated

name=(input("Enter a name :"))
num = (int(input("enter a number:")))
a,b=map(int,input("enter two numbers:").split())
def get_name():
    k= name
    return k
print("your name is ",get_name())

def divisibility(x):
    if x % 5 == 0:
        print("this given number is divisible by 5")
    else:
        print("this given number is not divisible by 5")
    return x
divisibility(num)



def summing(a,b):
    i=1
    sum1=0
    while i<=a:
        sum1=sum1+i
        i+=1
    i = 1
    sum2 = 0
    while i<=b:
        sum2 = sum2 + i
        i += 1
    return sum1+sum2
total=summing(a,b)
print ("Sum of two:",total)
