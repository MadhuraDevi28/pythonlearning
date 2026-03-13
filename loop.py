# write a program to get sum of the previous number for the given input.
# input=7
# expected output=28

n=7 #input
i=1 #assign 1  to a variable to compare
sum=0#initializing a variable
while i<=n:#we while  loop to loop until our condition satisfy & we can neither use for loop also
    sum=sum+i#here it sum the each i value until it reach the i<=n
    i+=1#it increment the value of i
print(sum)

