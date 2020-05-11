# function (f), example from lesson 5
# def f(a, b=True, *args, **kwargs):
#     print(a)
#     if b:
#         return args
#     return kwargs
#
#
# print(f(5, False, 1, 2, **{'name': 'test'}))


# class
# class Baloon:
#     pass
#
#
# baloon1 = Baloon()
# baloon2 = Baloon()
# baloon3 = Baloon()
#
# baloon1.color = 'cherry'
# baloon2.color = 'carrot'
# baloon3.color = 'blueberry'
#
# print(baloon1.color)
# print(baloon2.color)
# print(baloon3.color + '&' + baloon2.color + '&' + baloon1.color)
#
#
# class Dog:
#     def __init__(self, color):
#         self.color = color
#
#     def drink(self, water):
#         print(f'The Dog likes to drink {water}')
#
#
# dog = Dog('Golden')
# print(dog.color)
# dog.drink('fanta')
#
# # var1
# d = dict(name="Coconuts")
# print(d.get('name'))
#
#
# class MyDict(dict):
#     def get(self, key, default="dog"):
#         return super().get(key, default)


#newmethod
class Vehicle:
    def __init__(self, color, fuel):
        self.color = color
        self.fuel = fuel

    def display_your_fuel_type(self):
        print(f'Fuel: {self.fuel}')

    def sound(self, sound):
        print(f'{sound} trrtttrrrttr')

    def open_trunk(self):
        print('The doors are opened')

    def open_windows(self):
        print('The windows are closed')


car1 = Vehicle('red', 'petrol')
print('car1-fuel: ', car1.fuel)
print('car1-color: ', car1.color)
car1.display_your_fuel_type()
car1.sound('Sound is: ')
car1.open_trunk()
car1.open_windows()
print(' ')
car2 = Vehicle('black', 'diezel')
print('car2-color: ', car2.color)
print('car2-fuel: ', car2.fuel)
car2.display_your_fuel_type()
car2.sound('Sound is: ')
car2.open_windows()


#newclass
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f'Name: {self.name} Age: {self.age}')

    def __str__(self):
        return f'Name is {self.name}'

class Employee(Human):

    def __init__(self, name, age, company):
        super().__init__(name, age)
        self.company = company

    def display_info(self):
        super().display_info()
        print(f'Company:{self.company}')

class Student(Human):
    def __init__(self, name, age, university):
        super().__init__(name, age)
        self.university = university

    def display_info(self):
        super().display_info()
        print (f'Student {self.name} study in {self.university}')

people = [Human('Lola', 32), Student('Manana', 25, 'UTM'), Employee('Coco', 25, 'ASE')]

for human in people:
    human.display_info()
    print(people)