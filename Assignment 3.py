# Make a calculator using Python with addition , subtraction , multiplication , division and power.

'''a=int(input("Enter 1st Number:"))
b=int(input("Enter 2nd Number:"))
op=int(input("Enter Operation:"))
if op==1:
    add=a+b
    print(add)
elif op==2:
    sub=a-b
    print(sub)
elif op==3:
    mult=a*b
    print(mult)
elif op==4:
    div=a/b
    print(div)
elif op==5:
    power=a**b
    print(power)'''

# Write a program to check if there is any numeric value in list using for loop

'''testList = [1, 7, "a", 5, "H", 7]

def parseIntegers(mixedList):
    newList = [i for i in mixedList if isinstance(i, int)]
    print(newList)

parseIntegers(testList)'''

#Write a Python script to add a key to a dictionary

'''d = {5:10, 6:20}
d.update({8:30})
print(d)'''

#Write a Python program to sum all the numeric items in a dictionary

'''def Sum(myDict):
    sum = 0
    for i in myDict:
        sum = sum + myDict[i]
    return sum
d = {'a': 10, 'b': 20, 'c': 30}
print(Sum(d))'''

# Write a program to identify duplicate values from list

'''def Repeat(x):
    size = len(x)
    repeated = []
    for i in range(size):
        k = i + 1
        for j in range(k, size):
            if x[i] == x[j] and x[i] not in repeated:
                repeated.append(x[i])
    return repeated



l= [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
print(Repeat(l))'''

# Write a Python script to check if a given key already exists in a dictionary

d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def key(x):
  if x in d:
      print('Key is present in the dictionary')
  else:
      print('Key is not present in the dictionary')
key(5)
key(9)