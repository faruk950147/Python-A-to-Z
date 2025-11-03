# duck typing is a concept in Python that states that the type or class of an object is less important than the methods and attributes it has. 
class Duck:
    def quack(self):
        print("Quack quack!")

class Person:
    def quack(self):
        print("I can quack too!")

def make_it_quack(being):
    being.quack()  # We don’t care if it’s Duck or Person

d = Duck()
p = Person()

make_it_quack(d)  # Output: Quack quack!
make_it_quack(p)  # Output: I can quack too!
