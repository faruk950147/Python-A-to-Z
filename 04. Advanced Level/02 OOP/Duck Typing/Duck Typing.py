# Duck Typing হলো Python-এর একটি concept যেখানে object-এর type না দেখে তার 
# behavior (method/attribute আছে কিনা) দেখা হয়।

# সহজভাবে:

# “If it looks like a duck, swims like a duck, and quacks like a duck — then it is a duck”

# Python এ মানে:
# object কোন class-এর সেটা important না
# সে কী করতে পারে (methods) সেটাই important

# Example
class Duck:
    def sound(self):
        return "Quack"

class Dog:
    def sound(self):
        return "Bark"

def make_sound(animal):
    print(animal.sound())

duck = Duck()
dog = Dog()

make_sound(duck)  # Quack
make_sound(dog)   # Bark


# এখানে কী হলো?
# Python check করেনি Duck না Dog
# শুধু দেখেছে → sound() method আছে কিনা
# থাকলে কাজ করে ফেলেছে
# Key Point

# ✔ No strict type checking
# ✔ Focus on behavior, not type
# ✔ Very flexible (Python-এর power)

# Real-life example
# len("Hello")   # string
# len([1,2,3])   # list

# দুটো আলাদা type, কিন্তু দুজনেই len() support করে