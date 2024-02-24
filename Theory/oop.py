"""
The pillars of Object-Oriented Programming (OOP) are fundamental concepts that help organize and structure code around objects. 
The four main pillars of OOP are:

Encapsulation: Is the concept of grouping data (attributes) and methods (behaviors) that operate on that data into a single unit, called a class.
Objective: Restrict direct access to the internal implementation details and promote privacy. This allows controlling how data is manipulated and changed.

Inheritance: is a mechanism that allows a class (subclass or derived class) to inherit characteristics and behaviors from another class (superclass or base class).
Objective: Promote code reuse, establish class hierarchies, and facilitate code maintenance and extension.

Polymorphism: Polymorphism means "many forms." In OOP, it refers to the ability of objects from different classes to be treated uniformly through common interfaces.
Objective: Simplify object manipulation by allowing different classes to provide specific implementations for the same methods. This makes the code more flexible and extensible.

Abstraction: is the process of simplifying unnecessary complexities. In OOP, a class is a form of abstraction that models real-world objects, highlighting only relevant aspects.
Objective: Provide a simplified and efficient representation of real-world concepts, allowing developers to focus on important details and ignore irrelevant ones.
"""


class Animal:
    class_variable = "I am a class variable"

    def __init__(self, voice):
        self.voice = voice


if __name__ == "__main__": 
    cat = Animal("Meeow")
    dog = Animal("Woof")

    print(cat.voice)
    print(dog.voice)
    print(cat.class_variable)
    print(dog.class_variable)

class Animal:
    def make_sound(self):
        pass


class Cat(Animal):
    def make_sound(self):
        return "Meoow"


class Dog(Animal):
    def make_sound(self):
        return "Woof"
    

if __name__ == "__main__": 
    cat = Cat()
    dog = Dog()

    print(cat.make_sound())
    print(dog.make_sound())


# things to complete here, private, public, context manager, decorators, magic methods, abstract with ABC