#Write a code in python in which create a class named it Car which have
#5 attributes such like(model, color and name etc.) and 3 methods.
#And create 5 object instance from that class.

class Car:
    def __init__(self,model,color,name,wheel,seats):
        self.model=model
        self.color=color
        self.name=name
        self.wheel=wheel
        self.seats=seats
    def truck(Car,model,color,name,wheel,seats):
        super().__init__(model,color,name,wheel,seats)
    def taxi(Car):
        super().__init__(model,color,name,wheel,seats)
    def rickshaw(Car):
        super().__init__(model,color,name,wheel,seats)

car=Car('BMW','red','HERO',4,4)
car.truck()
car.taxi()
car.rickshaw()
