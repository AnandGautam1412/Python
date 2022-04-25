#Question 1

q=int(input("Enter 1st number : "))
w=int(input("Enter 2nd number : "))
e=int(input("Enter 3rd number : "))
print("Average of the numbers : ",(q+w+e)/3)





#Question 2

income=int(input("Enter Gross Income : "))
depends=int(input("Enter the number of dependents :"))
taxable_amount=income-10000-(3000*depends)
tax=taxable_amount*0.2
print("Tax to be paid : ",tax)




#Question 3

q=input("Enter the name of the person : ")
w=int(input("Enter the age of the person : "))
e=float(input("Enter the marks obatined by the person : "))
r=input("Enter the name of the course peson wants to take : ")
t=int(input("Enter the SID of the students : "))
y=[q,w,e,r,t]
print("Information about the person :",y)





#Question 4


q=int(input("Enter the marks of 1st student : "))
w=int(input("Enter the marks of 2nd student : "))
e=int(input("Enter the marks of 3rd student : "))
r=int(input("Enter the marks of 4th student : "))
t=int(input("Enter the marks of 5th student : "))
y=[q,w,e,r,t]
print("Marks of the students : ",y)
y.sort()
print("Marks of the students in the sorted manner : ",y)






#Question 5


list=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
list.pop(3)
print(list)


list=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
list=["Purple" if(i=="Black")or(i=="Pink")else i for i in b1]
print(list)




