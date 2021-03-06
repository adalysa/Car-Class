#Adalysa Rosales
#3/5/2021
#Lab 3

class Car:

    def __init__(self, make, year_model):
        self.__make=make
        self.__year_model=year_model
        self.__speed=0

    def accelerate(self):
        self.__speed+=5

    def brake(self):
        self.__speed-=5

    def get_speed(self):
        return self.__speed


car=Car('Mazda', '2011')

for i in range(5):
    car.accelerate()
    speed=car.get_speed()
    print(speed)

for i in range(5):
    car.brake()
    speed=car.get_speed()
    print(speed)