# class Car:
#     def __init__(self, model, year, color, forsale):
#         self.model = model
#         self.year = year
#         self.color = color
#         self.forsale = forsale

#     def display_info(self):
#         return f"{self.model} {self.year} {self.color} {self.forsale}"

#     def drive(self):
#         return "Driving " + self.model

#     def sell(self):
#         if self.forsale:
#             return f"Selling a {self.year} {self.color} {self.model}"
#         else:
#             return "Not for sale"

# car1 = Car("Toyota", 2019, "Red", True)
# # print(car1) # returns the address of the object
# print(car1.model)

# car2 = Car("Ford", 2020, "Blue", False)
# print(car2.display_info())
# print(car1.drive())
# print(car1.sell())
# print(car2.sell())

# Class variables
# class Student:
#     total_students = 0
#     class_year = 2020

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         Student.total_students += 1

# student1 = Student("John", 20)
# student2 = Student("Jane", 21)
# student3 = Student("Jack", 22)
# print(student1.class_year)
# print(Student.class_year) # better practice
# print(Student.total_students)

# Inheritance
# class Animal:
#     def __init__(self, name):
#         self.name = name
#         self.isalive = True

#     def eat(self):
#         return f"{self.name} is eating"

#     def sleep(self):
#         return f"{self.name} is sleeping"
# class Dog(Animal):
#     def bark(self):
#         return "Woof Woof"
# class Cat(Animal):
#     def meow(self):
#         return "Meow Meow"
# dog = Dog("Buddy")
# print(dog.eat())
# print(dog.bark())
# cat = Cat("Kitty")
# print(cat.sleep())
# print(cat.meow())

# Multiple inheritance &  Multilevel inheritance
# class Prey(Animal):
#     def flee(self):
#         return "Prey is fleeing"
# class Predator(Animal):
#     def hunt(self):
#         return "Predator is hunting"
# class Rabbit(Prey):
#     pass
# class Hawk(Predator):
#     pass
# class Fish(Prey, Predator):
#     pass
# rabbit = Rabbit()
# print(rabbit.flee())
# print(rabbit.eat())
# # print(rabbit.hunt()) # error
# hawk = Hawk()
# # print(hawk.flee()) # error
# print(hawk.hunt())
# fish = Fish()
# print(fish.flee())
# print(fish.hunt())

# Super function
# class Shape:
#     def __init__(self, color, filled):
#         self.color = color
#         self.filled = filled
# class Circle(Shape):
#     def __init__(self, radius, color, filled):
#         self.radius = radius
#         super().__init__(color, filled)
# class Square(Shape):
#     def __init__(self, side, color, filled):
#         self.side = side
#         super().__init__(color, filled)
# class Triangle(Shape):
#     def __init__(self, base, height, color, filled):
#         self.base = base
#         self.height = height
#         super().__init__(color, filled)
# circle = Circle(5, "Red", True)
# print(circle.color)
# print(circle.filled)
# print(circle.radius)
# square = Square(4, "Blue", False)
# print(square.color)

# Polymorphism
# Using inheritance
# from abc import ABC, abstractmethod
# class Shape:
#     @abstractmethod
#     def area(self):
#         pass
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#     def area(self):
#         return 3.14 * self.radius * self.radius
# class Square(Shape):
#     def __init__(self, side):
#         self.side = side
#     def area(self):
#         return self.side * self.side
# class Pizza(Circle):
#     def __init__(self, toppings, radius):
#         super().__init__(radius)
#         self.toppings = toppings
# shapes = [Circle(5), Square(4), Pizza(["Cheese"], 10)]
# # Pizza has 3 forms : Pizza , Circle , Shape
# for shape in shapes:
#     print(shape.area())
# Using duck typing
# class Animal():
#     alive = True
# class Dog(Animal):
#     def speak(self):
#         return "Woof Woof"
# class Cat(Animal):
#     def speak(self):
#         return "Meow Meow"
# class Car:
#     alive = False
#     def speak(self):
#         return "Vroom Vroom"
# # Here car has the min basic requirements to be an animal
# animals = [Dog(), Cat(),Car()]
# for animal in animals:
#     print(animal.speak())
#     print(animal.alive)
# Static methods
# class Employee():
#     def __init__(self, name,position):
#         self.name = name
#         self.position = position
#     def get_info(self):
#         return f"{self.name} is a {self.position}"
#     @staticmethod # belong to the class not the object
#     def is_valid_position(position):
#         return position in ["Manager", "Developer", "Intern"]
# employee1 = Employee("John Doe", "Developer")
# print(employee1.get_info())
# print(Employee.is_valid_position("Developer"))
# print(Employee.is_valid_position("CEO"))

# Class methods
# class Student():
#     count = 0
#     total_gpa = 0
#     def __init__(self, name, gpa):
#         self.name = name
#         self.gpa = gpa
#         Student.count += 1
#         Student.total_gpa += self.gpa
#     def get_info(self):
#         return f"{self.name} has a GPA of {self.gpa}"
#     @classmethod # cls is the class itself -> to work with class data
#     def get_total_students(cls):
#         return cls.count
#     @classmethod
#     def get_average_gpa(cls):
#         if cls.count  != 0:
#             return cls.total_gpa / cls.count
# student1 = Student("John Doe", 3.8)
# print(student1.get_info())
# print(Student.get_total_students())
# print(Student.get_average_gpa())

# Magic methods def __function__(self):
# class Book():
#     def __init__(self, title, author, num_pages): # __init__
#         self.title = title
#         self.author = author
#         self.num_pages = num_pages
#     def __str__(self): # __str__ -> to change behaviour while printing book
#         return f"Title: {self.title}, Author: {self.author}, Number of Pages: {self.num_pages}"
#     def __eq__(self, other):
#         return self.title == other.title and self.author == other.author
#     def __lt__(self, other):
#         return self.num_pages < other.num_pages
#     def __add__(self, other):
#         return self.num_pages + other.num_pages
#     def __contains__(self, item):
#         return item in self.title
#     # def __getitem__(self, index):
#     #     return self.title[index]
#     def __getitem__(self, key):
#         if key == 'title':
#             return self.title
#         elif key == 'author':
#             return self.author
#         elif key == 'num_pages':
#             return self.num_pages
#         else:
#             return "Invalid key"
# book1 = Book("Book 1","Author 1", 100)
# book2 = Book("Book 2","Author 2", 200)
# book3 = Book("Book 3","Author 3", 300)
# book4 = Book("Book 1","Author 1", 100)
# print(book1) # will call __str__ method # usually returns the address of the object
# print(book1==book4) # will call __eq__ method
# print(book1==book2)
# print(book2<book3) # will call __lt__ method
# print(book3+book2) # will call __add__ method
# print("Book 1" in book1) # will call __contains__ method
# # print(book1[2]) # will call __getitem__ method
# print(book1['title']) # will call __getitem__ method
