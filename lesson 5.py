#function (f), example from lesson 5

def f(a, b=True, *args, **kwargs):
    print(a)
    if b:
        return args
    return kwargs


print(f(5, False, 1, 2, **{'name': 'test'}))


#class
#pass - you dont declare anythong in this class
class Baloon:
    pass


baloon1 = Baloon()
baloon2 = Baloon()
baloon3 = Baloon()

baloon1.color = 'cherry'
baloon2.color = 'carrot'
baloon3.color = 'blueberry'

print(baloon1.color)
print(baloon2.color)
print(baloon3.color + '&' + baloon2.color + '&' + baloon1.color)


# newclass2
class Dog:
    def __init__(self, color):
        self.color = color

    def drink(self, water):
        print(f'The Dog likes to drink {water}')


dog = Dog('Golden')
print(dog.color)
dog.drink('fanta')

# var1
d = dict(name="Coconuts")
print(d.get('name'))


class MyDict(dict):
    def get(self, key, default="dog"):
        return super().get(key, default)


#newclass3
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


toyota = Vehicle('red', 'petrol')
print('car1-fuel: ', toyota.fuel)
print('car1-color: ', toyota.color)
toyota.display_your_fuel_type()
toyota.sound('Sound is: ')
toyota.open_trunk()
toyota.open_windows()
print(' ')

car2 = Vehicle('black', 'diezel')
print('car2-color: ', car2.color)
print('car2-fuel: ', car2.fuel)
car2.display_your_fuel_type()
car2.sound('Sound is: ')
car2.open_windows()


#newclass4
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f'Name: {self.name} Age: {self.age}')

    def __str__(self):
        return f'Name is {self.name}'


class Musician(Human):
    def __init__(self, name, age, instrument):
        super().__init__(name, age)
        self.instrument = instrument

    def display_info(self):
        super().display_info()
        print(f'Plays instrument: {self.instrument}')


class Dancer(Human):
    def __init__(self, name, age, dance):
        super().__init__(name, age)
        self.dance = dance

    def display_info(self):
        super().display_info()
        print(f'Dancer {self.name} prefers to dance {self.dance}')


people = [Human('Lola', 32), Dancer('Manana', 25, 'Tango'), Musician('Coco', 25, 'Violin')]

for human in people:
    human.display_info()
