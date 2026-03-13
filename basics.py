# # n=5
# # i=1
# # sum=0
# # while i<=n:
# #     sum = sum + i
# #     i += 1
# # print(sum)

# input=123
# output=6
# n=123
# rem=123%10(3)
# q=123//10(12=n)
#
# n=12
# rem=12%10(2)
# q=12//10(1=n)
#
# n=1
# rem=1%10(1)
# q=1//10(0=n)

# n=0
n=12345
sum=0
while n > 0:
    i = n % 10
    n//=10
    sum+=i
print(sum)

422