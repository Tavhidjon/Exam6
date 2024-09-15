### 1 Question
# Create a class Employee with a public attribute name, a protected attribute _salary, 
# and a private attribute __id. Demonstrate how these are accessed and restricted.

# Создайте класс Employee с публичным атрибутом name, защищенным атрибутом _salary 
# и закрытым атрибутом __id. Покажите, как они доступны и ограничены.

# class Employee:
#     def __init__(self,name,salary,id):
#         self.name=name
#         self._salary=salary
#         self.__id=id

#     def show(self):
#         if  self.__id==1134:

#             print(self.name,self._salary,self.__id)
#         else:
#             print("Incorrect Id")       
# obj1=Employee("Tavhid",1200,2344)
# obj1.show()






# ### 2 Question
# Create a class BankAccount with private attributes _balance and __pin.
# Initialize the values in the constructor.
# Access the _balance directly and see what happens when you try to access __pin.

# Создайте класс BankAccount с приватными атрибутами _balance и __pin.
# Инициализируйте значения в конструкторе.
# Получите доступ к _balance напрямую и посмотрите, что произойдет, когда вы попытаетесь получить доступ к __pin.
# class BankAccount:
#     def __init__(self,balance,pin):
#         self._balance=balance
#         self.__pin=pin
#     def show(self):
#         if self.__pin == 1234:
#             print(self._balance,self.__pin)
# obj1=BankAccount(20000,1234)
# obj1.show()


### 3 Question
# a) In the same BankAccount class, define a setter method to update the private attribute _balance.
# Ensure that balance can’t be negative by checking in the setter.
# В том же классе BankAccount определите метод-сеттер для обновления частного атрибута _balance.
# Убедитесь, что баланс не может быть отрицательным, проверив в сеттере.

# b) Create a class Employee with an instance attribute name and a class attribute company.
# Create two objects and modify the company class attribute. Print the result to observe the behavior.
# Создайте класс Employee с атрибутом экземпляра name и атрибутом класса company.
# Создайте два объекта и измените атрибут класса company. Распечатайте результат, чтобы понаблюдать за поведением.


# class BankAccount:
#     company="Softclub"
#     def __init__(self,name,balance):
#         self._balance=balance
#         self.name=name
#     def show(self):
#         print(self.name,self._balance)
    
# class Employee(BankAccount):
#     @classmethod
#     def __init__(cls):
#         cls.company="Alif"
#         cls.name="Khomid"
#     def show(self):
#         print(self.company,self.name)

# obj2=Employee()
# obj2.show()

        








### 4 Question
# Create a base class Animal with a method speak().
# Create a derived class Dog that overrides speak().
# Further, derive a class Puppy from Dog and override the speak() method again.
# Call the speak() method from a Puppy object.

# Создайте базовый класс Animal с методом speak().
# Создайте производный класс Dog, который переопределяет speak().
# Далее, выведите класс Puppy из Dog и снова переопределите метод speak().
# Вызовите метод speak() из объекта Puppy.


# class Animal:
#     def speak(self):
#         print("Gaf-Gaf")
# class Dog(Animal):
#     pass
# class Puppy(Dog):
#     pass

# obj3=Puppy().speak()




### 5 Question
# Write a Python program to create a person class. Include attributes like name, country and date of birth.
#  Implement a method to determine the person's age. Use incapsulation methods as well. / Напишите программу на 
#  Python для создания класса человека. Включите такие атрибуты, как имя, страна и дата рождения. Реализуйте метод 
#  определения возраста человека. Также используйте методы инкапсуляции.



# class Person:
#     def __init__(self,name,country,date_of_birth):
#         self.name=name
#         self.country=country
#         self.date_of_birth=date_of_birth     
#     def show(self):
#         print(f"Name:{self.name},'\n' Country: {self.country},'\n' Date of birth:{self.date_of_birth}")
# obj1=Person("Tavhid","Dushanbe",2006)
# obj1.show()
    




# ### 6 Question
# Build a Nobel class. An instance is already created for you and instance attributes are included inside the print. Take those clues and try to reverse engineer the class.  Implement string representation of a class object using str method inside the class.

# Создайте Nobel класс. Экземпляр уже создан для вас, и атрибуты экземпляра включены в результат print. 
# Воспользуйтесь этими подсказками и попытайтесь спроектировать класс. Реализуйте строковое представление 
# объекта класса, используя метод __str__ внутри класса.
# ```
# class Nobel:
#     pass

# np2005=Nobel("Peace", 2005, "Muhammad Yunus")

# print(np2005.category, np2005.year, np2005.winner)



# class Nobel:
#     def __init__(self,Catagory,year,Winner):
#           self.Catagory=Catagory
#           self.year=year
#           self.Winner=Winner
#     def __str__(self):
#          print(f"{self.Catagory} , {self.year} , {self.Winner}")
# obj1=Nobel("Salom",2006,"Tavhid")
# obj1.__str__()
    
        

### 7 Question
# Create a function which returns "upper" if all the letters in a word are uppercase, "lower" if lowercase and "mixed" for any mix of the two.
# Создайте функцию, которая возвращает «верхнюю», если все буквы в слове прописные, «нижнюю»,
#  если строчные, и «смешанную» для любого сочетания   этих двух букв.

# getCase("whisper...") ➞ "lower"

# getCase("SHOUT!") ➞ "upper"




# def harf(a):
#         if a.islower():
#             print("lower")
#         elif a.isupper():
#             print("Upper")
#         else:
#             print('Mixed')
# print(harf(input()))




# Print the following pattern.(Распечатайте следующий шаблон.)
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
# 6 6 6 6
# 7 7 7
# 8 8
# 9


a=int(input())
b=a//2
for i in range(b):
        i+=1
        if i==b:
              i-=1
        print(i)



# print('''
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
# 6 6 6 6
# 7 7 7
# 8 8
# 9
#       ''')





        
    


    
