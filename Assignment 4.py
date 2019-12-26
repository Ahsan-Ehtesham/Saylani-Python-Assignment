<<<<<<< HEAD
#Ques1:

'''dict={
    'first_name':input("Enter First Name:"),
    'last_name':input("Enter Last Name:"),
    'age':int(input("Enter Age:")),
    'city':input("Enter City:")
}
print(dict)
dict["qualification"]="High Academic Level"
print(dict)
del dict["qualification"]
print(dict)'''

#Ques2:

'''cities={
    'Karachi':{
        'country':"Pakistan",
        'population':"14.91 million",
        'fact':"It is the Sixth largest city in the world by city population."
    },
    'NewYork':{
        'country':"USA",
        'population':"8.623 million",
        'fact':"It was originally called Longacre Square."
    },
    'London':{
        'country':"UK",
        'population':"8.9 million",
        'fact':"It has the iconic 'Big Ben' clock tower."
    }
}
print(cities['Karachi'])
print(cities['NewYork'])
print(cities['London'])'''

#Ques3:

'''while True:
    age = int(input("Enter Age:"))
    if age<=3:
        print('Ticket is free')
    elif age>3 and age<=12:
        print('Ticket is $10')
    else:
        print('Ticket is $15')'''

#Ques4:

def favorite_book(title):
    print('One of my favorite books is',title)

favorite_book('Batman')

#Ques5: Guess the number game

import random
count = 0
x = random.randint(1, 30)
#print(x)
for count in range(3):
    num = int(input("Enter Number b/w 1 to 30:"))
    if num==x:
        print("Correct")
        break
    elif x>num:
        print("Hidden num is greater")
    elif x<num:
        print("Hidden num is smaller")

=======
#Ques1:

'''dict={
    'first_name':input("Enter First Name:"),
    'last_name':input("Enter Last Name:"),
    'age':int(input("Enter Age:")),
    'city':input("Enter City:")
}
print(dict)
dict["qualification"]="High Academic Level"
print(dict)
del dict["qualification"]
print(dict)'''

#Ques2:

'''cities={
    'Karachi':{
        'country':"Pakistan",
        'population':"14.91 million",
        'fact':"It is the Sixth largest city in the world by city population."
    },
    'NewYork':{
        'country':"USA",
        'population':"8.623 million",
        'fact':"It was originally called Longacre Square."
    },
    'London':{
        'country':"UK",
        'population':"8.9 million",
        'fact':"It has the iconic 'Big Ben' clock tower."
    }
}
print(cities['Karachi'])
print(cities['NewYork'])
print(cities['London'])'''

#Ques3:

'''while True:
    age = int(input("Enter Age:"))
    if age<=3:
        print('Ticket is free')
    elif age>3 and age<=12:
        print('Ticket is $10')
    else:
        print('Ticket is $15')'''

#Ques4:

def favorite_book(title):
    print('One of my favorite books is',title)

favorite_book('Batman')

#Ques5: Guess the number game

import random
count = 0
x = random.randint(1, 30)
#print(x)
for count in range(3):
    num = int(input("Enter Number b/w 1 to 30:"))
    if num==x:
        print("Correct")
        break
    elif x>num:
        print("Hidden num is greater")
    elif x<num:
        print("Hidden num is smaller")

>>>>>>> dbbb3ca09038ae69ce39e8a60c23e87d1d11865b
