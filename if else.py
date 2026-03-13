#write a program to get a student name and mark and display the name of the student with their regarding grade
n = (input("Enter your Name:")) #we get a input from the user and no need to put the print
m = (int(input("Enter your Mark:")))#same as name
print("Name :",n)
if m in range(95,101):#if the give mark is between this range it satisfies the stmt ang prints
    print("Your grade is A ")
elif m in range(85,95):#if not it satisfies the if stmt it comes to elif and look for the range if not move to next
    print("Your grade is B ")
elif m in range(75, 85):
    print("Your grade is C ")
elif m in range(65,75):
    print("Your grade is D ")
elif m in range(50,65):
    print("Your grade is E ")
else:#if not it satisfy any stmt it comes to else
    print("you are fail")
