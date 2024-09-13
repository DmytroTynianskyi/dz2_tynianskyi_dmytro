# Завдання 1
# Створіть клас, який описує автомобіль. Які атрибути та методи мають бути повністю інкапсульовані?
# Доступ до таких атрибутів та зміну даних реалізуйте через спеціальні методи(get, set).

class Auto:
    def __init__(self, make: str, model: str, year: int, color: str, mileage: int):
        self.__make = make       
        self.__model = model     
        self.__year = year        
        self.color = color      
        self.mileage = mileage  
    
    def get_auto(self):
        return f"{self.__year} {self.__make} {self.__model}, Колір: {self.color}, Пробіг: {self.mileage} км"

    def get_make(self):
        return self.__make
    
    def get_model(self):
        return self.__model
    
    def get_year(self):
        return self.__year
    
    def set_make(self,new_make:str):
        self.__make =new_make
        return self.__make

    def set_model(self,new_model:str):
        self.__model = new_model
        return self.__model

    def set_year(self,new_year:int):
        self.__year = new_year
        return self.__year

my_car = Auto("Toyota", "Camry", 2020, "Червоний", 10000)
print(my_car.get_auto())








