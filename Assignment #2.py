<<<<<<< HEAD
# Program # 1
# Write a program which takes 5 inputs from user for different subject’s marks, total it and generate mark sheet using grades ?

a=int(input("Enter Subject 1 Marks:"))
b=int(input("Enter Subject 2 Marks:"))
c=int(input("Enter Subject 3 Marks:"))
d=int(input("Enter Subject 4 Marks:"))
e=int(input("Enter Subject 5 Marks:"))
total=((a+b+c+d+e)/500)*100
if total>=80 and total<100:
    print("A")
elif total>=70 and total<80:
    print("B")
elif total>=60 and total<70:
    print("C")
elif total>=50 and total<60:
    print("D")
elif total<50:
    print("Fail")

# Program # 2
# Write a program which take input from user and identify that the given number is even or odd?

a=int(input("Enter a Number:"))
if a%2==0:
    print("Even")
else:
    print("Odd")

# Program # 3
# Write a program which print the length of the list?

L=[1,2,3,5,6,7,8,10]
print(len(L))

# Program # 4
# Write a Python program to sum all the numeric items in a list?

L=[]
n=int(input("Enter no of elements:"))
for i in range(n):
    element=int(input("Enter Element:"))
    L.append(element)
print(L)
print(sum(L))


# Program # 5
# Write a Python program to get the largest number from a numeric list.

L=[2,4,6,7,8,9,10]
print(max(L))

# Program # 6
# write a program that prints out all the elements of the list that are less than 5.

L=[]
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for x in a:
    if x<5:
        L.append(x)
=======
# Program # 1
# Write a program which takes 5 inputs from user for different subject’s marks, total it and generate mark sheet using grades ?

a=int(input("Enter Subject 1 Marks:"))
b=int(input("Enter Subject 2 Marks:"))
c=int(input("Enter Subject 3 Marks:"))
d=int(input("Enter Subject 4 Marks:"))
e=int(input("Enter Subject 5 Marks:"))
total=((a+b+c+d+e)/500)*100
if total>=80 and total<100:
    print("A")
elif total>=70 and total<80:
    print("B")
elif total>=60 and total<70:
    print("C")
elif total>=50 and total<60:
    print("D")
elif total<50:
    print("Fail")

# Program # 2
# Write a program which take input from user and identify that the given number is even or odd?

a=int(input("Enter a Number:"))
if a%2==0:
    print("Even")
else:
    print("Odd")

# Program # 3
# Write a program which print the length of the list?

L=[1,2,3,5,6,7,8,10]
print(len(L))

# Program # 4
# Write a Python program to sum all the numeric items in a list?

L=[]
n=int(input("Enter no of elements:"))
for i in range(n):
    element=int(input("Enter Element:"))
    L.append(element)
print(L)
print(sum(L))


# Program # 5
# Write a Python program to get the largest number from a numeric list.

L=[2,4,6,7,8,9,10]
print(max(L))

# Program # 6
# write a program that prints out all the elements of the list that are less than 5.

L=[]
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for x in a:
    if x<5:
        L.append(x)
>>>>>>> dbbb3ca09038ae69ce39e8a60c23e87d1d11865b
print(L)