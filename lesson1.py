#Основные понятия ООП:
#Класс — это как чертёж. Он описывает, как должен выглядеть объект (что у него есть и что он умеет).

#Объект — это экземпляр класса. То есть конкретная «вещь», созданная по чертежу.

#Метод — это функция внутри класса.

#Атрибут — это переменная внутри объекта.


class Person: # класс чертеж 
    def __init__(self, name, age): # __init__ конструктор
                #сам объект 
        self.name = name 
        self.age = age
    # функция внутри класса это уже метод
    def greet(self):
        print(f"Привет, меня зовут {self.name} и мне {self.age}")

#person1 = Person("Ислам", 21)
#person1.greet()

#person2 = Person("Geeks", 4)
#person2.greet()


class CAR:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model 
        self.year = year
        self._engine_on = False

    def start_engine(self):
        if not self._engine_on:
            self._engine_on = True
            print(f"{self.brand} {self.model}: Двигатель запущен.")
        else:
            print(f"{self.brand} {self.model}: Двигатель уже работает")

    def stop_engine(self):
        if not self._engine_on:
            self._engine_on = False
            print(f"{self.brand} {self.model}: Двигатель заглушен.")
        else:
            print(f"{self.brand} {self.model}: Двигатель уже выключен")
    
    def info(self):
        print(f"Машина: {self.brand} {self.model} ({self.year})")

#car = CAR("Toyota", "Camry", 2022)
#car.info()
#car.start_engine()
#car.start_engine()
#car.stop_engine()
#car.stop_engine()



#Наследование — возможность создавать новый класс на
#  основе существующего. 
# Дочерний класс получает свойства и методы родительского.

class Animal:
    def speak(self):
        print("Животное издает звук")

class Dog(Animal):
    def speak(self):
        print("Собака лает")

class Cat(Animal):
    def speak(self):
        print("Кошка мяукает")

#a = Animal()
#a.speak()
#
#d = Dog()
#d.speak()
#
#c = Cat()
#c.speak()

#Родительский класс персон
class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Меня зовут {self.name}")

class Student(Person):
#дочерний класс студент
    def __init__(self, name, group):
        #вызываем конструктор родительского класса
        super().__init__(name) 
        self.group = group
    #перезапишим метов introduce
    def introduce(self):
        print(f"Меня зовут {self.name}, моя группа - {self.group}")

p = Person("Абдурашит")
p.introduce()

s = Student("Джек", "B12")
s.introduce()
