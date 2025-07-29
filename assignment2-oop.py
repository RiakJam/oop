class Animal:
    def move(self):
        raise NotImplementedError("Subclasses must implement move()")

class Cheetah(Animal):
    def move(self):
        return "Running at 70 mph! 🐆"

class Dolphin(Animal):
    def move(self):
        return "Swimming through waves! 🐬"

class Eagle(Animal):
    def move(self):
        return "Soaring above mountains! 🦅"

# Polymorphic function
def animal_race(animals):
    for animal in animals:
        print(animal.move())

# Usage
creatures = [Cheetah(), Dolphin(), Eagle()]
animal_race(creatures)
"""
Running at 70 mph! 🐆
Swimming through waves! 🐬
Soaring above mountains! 🦅
"""