#write a program to find sum of digits for given input.
#Given input=124568
#expected output=26

n=124568
sum=0
while n>0:
    i=n%10
    n//=10
    sum+=i
print(sum)