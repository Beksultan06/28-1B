# from abc import ABC, abstractmethod

# class PaymentMethod(ABC):

#     @abstractmethod
#     def authenticate(self):
#         pass

#     @abstractmethod
#     def pay(self):
#         pass

# class CreditCardPayment(PaymentMethod):
#     def authenticate(self):
#         print("Проверка данных кредитной карты")

#     def pay(self, amount):
#         print(f"Оплата {amount}$ через PayPal прошла успешно")

# class PaypalPayment(PaymentMethod):
#     def authenticate(self):
#         print("Вход в Аккаунт")

#     def pay(self, amount):
#         print(f"Оплата {amount}$ через PayPal прошла успешно")

# class CryptoPayment(PaymentMethod):
#     def authenticate(self):
#         print("Проверка криптокошелька")

#     def pay(self, amount):
#         print(f"Оплата {amount}$ через криптовалюту прошла успешно")


# def payment(payment_method: PaymentMethod, amount: float):
#     payment_method.authenticate()
#     payment_method.pay(amount)

# credit_card = CreditCardPayment()
# paypal = PaypalPayment()
# crypto = CryptoPayment()
# 
# payment(credit_card, 100)
# payment(crypto, 500)
# payment(paypal, 1000)


# class Parent1:
#     pass

# class Parent2:
#     pass

# class Child(Parent1, Parent2):
#     pass 


# class Printer:
#     def print_doc(self, document):
#         print(f"Печатаеть документа: {document}")

# class Scanner:
#     def scan_doc(self):
#         print("Сканирование документа")

# class All(Printer, Scanner):
#     pass

# device = All()
# device.print_doc("test.txt")
# device.scan_doc()


class Cleaner:
    def work(self):
        print("Убираю комнату")

class Cook:
    def work(self):
        print("Готовлю еду")

class Roobat(Cleaner, Cook):
    def work(self):
        print("Работ начитает работу!")
        Cook.work(self)
        Cleaner.work(self)
        print("Робот завершил работу!")

robot = Roobat()
robot.work()
print(Roobat.mro())