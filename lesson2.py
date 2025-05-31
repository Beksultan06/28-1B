# В контексте объектно-ориентированного 
# программирования (ООП) термин инкарнация
# означает создание конкретного экземпляра (объекта)
# из класса.


# class Dog:
#     def __init__(self, name):
#         self.name = name

# dog = Dog("Ак тош")
# print(dog.name)


# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance
# 
#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#     
#     def withdraw(self, amount):
#         if 0 < amount <= self.__balance:
#             self.__balance -= amount
# 
#     def get_balance(self):
#         return self.__balance

# acc = BankAccount(1000)
# 
# acc.deposit(500)
# acc.withdraw(300)
# print(acc.get_balance())
# print(acc.__balance)

# class Bank:
#     def __init__(self, owner_name, initial_balance, pin_code):
#         self.owner_name = owner_name
#         self._balance = initial_balance
#         self.__pin_code = pin_code

#     def show_owner(self):
#         print(f"Владелец счёта : {self.owner_name}")

#     def get_balance(self):
#         print(f"Текущий баланс : {self._balance} сом")

#     def deposit(self, amount):
#         if amount > 0:
#             self._balance += amount
#             print(f"Пополнено : {amount} сом")
#         else:
#             print("Сумма должно быть положительным")

#     def withdraw(self, amount):
#         if amount <= 0:
#             print("Сумма должна быть положительным")
#         elif amount > self._balance:
#             print("Недостаточно средств")
#         else:
#             self._balance -= amount
#             print(f"Снято : {amount} сомов")

#     def __show_pin(self):
#         print(f"PIN-код : {self.__pin_code}")

#     def verify_identity(self, entered_pin):
#         if entered_pin == self.__pin_code:
#             print("Пин code верный")
#         else:
#             print("Неверный пин код")


# acc = Bank("Maikl", 5000, "1234")
# print(Bank.mro())
# acc.show_owner()
# acc.get_balance()
# acc.deposit(1500)
# acc.withdraw(1000)
# acc.get_balance()

#print(acc._balance)
#
#acc.verify_identity("0000")
#acc.verify_identity("1234")
#
#print(acc._Bank__pin_code)

# Полиморфизм — это возможность использовать один и тот же интерфейс 
# (метод) для объектов разных классов, 
# при этом каждый объект выполняет своё собственное поведение.

# class Dog:
#     def speak(self):
#         print("Gav")

# class Cat:
#     def speak(self):
#         print("Мяу")

# def animal_sound(animal):
#     animal.speak()

# dog = Dog()
# cat = Cat()

# animal_sound(dog)
# animal_sound(cat)


# class Animal:
#     def make_sound(self):
#         print("Животное издает звук")

# class Dog(Animal):
#     def make_sound(self):
#         print("Gav")

# class Cat(Animal):
#     def make_sound(self):
#         print("Мяу")

# animals = [Dog(), Cat(), Animal()]

# for animal in animals:
#     animal.make_sound()