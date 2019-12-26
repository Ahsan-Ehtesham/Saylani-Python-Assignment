#Write a code in python in which create a class named it Car which have
#5 attributes such like(model, color and name etc.) and 3 methods.
#And create 5 object instance from that class.

class Car:
    def __init__(self,model,color,year,wheel,seats):
        self.model=model
        self.color=color
        self.year=year
        self.wheel=wheel
        self.seats=seats

bmw=Car('BMW','Blue','2000','4','4')
ferrari=Car('Ferrari','red','1999','4','4')
honda=Car('Honda','Black','2009','4','5')
print(ferrari.color)
print(honda.seats)

