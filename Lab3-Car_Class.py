#Adalysa Rosales
#3/5/2021
#Lab 3

class Car:

    def __innit__(self, make, year_model):
        self.__make=make
        self.__year_model=yaer_model
        self.__speed=0

    def accelerate(self):
        self.__speed+=5

    def brake(self):
        self.__speed-=5

    def get_speed(self):
        return self.__speed