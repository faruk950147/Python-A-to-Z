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

# Duck Typing vs Static Typing (Python vs Java/C++) খুব সহজভাবে বুঝি।

# Duck Typing (Python)

# Type আগে check করা হয় না
# কাজ করে object-এর behavior দেখে

# উদাহরণ (Python)
def add(x, y):
    return x + y

print(add(5, 10))       # 15
print(add("A", "B"))    # AB

# এখানে একই function দুইভাবে কাজ করছে
# int যোগ
# string join

# কারণ Python শুধু দেখে + কাজ করতে পারছে কিনা

# Static Typing (Java / C++)

# Type আগে থেকেই fixed
# Compile time এ check হয়

# উদাহরণ (Java)
# int add(int x, int y) {
#     return x + y;
# }

# এখানে শুধু int allowed
# string দিলে error হবে

# Comparison
# Feature	Duck Typing (Python)	Static Typing (Java/C++)
# Type check	Runtime	Compile time
# Flexibility	খুব বেশি	কম
# Error detect	পরে ধরা পড়ে	আগেই ধরা পড়ে
# Coding speed	দ্রুত	তুলনামূলক ধীর
# Safety	কম strict	বেশি safe
# সহজ মনে রাখার trick

# Duck Typing = “কি পারে সেটা দেখো”
# Static Typing = “কি টাইপ সেটা আগে ঠিক করো”

# Bottom line
# Python → flexible & fast development
# Java/C++ → strict & safe programs

# এবার বুঝি Python internally কীভাবে Duck Typing / Dynamic Typing handle করে

# Python কীভাবে কাজ করে (Internally)

# Python এ কোনো variable-এর type আগে থেকে fix থাকে না।

# Python সব কিছুকে object হিসেবে ধরে
# type check করা হয় runtime এ

# Example
x = 10
x = "Hello"

# এখানে কী হলো?

# প্রথমে x → int object (10)
# পরে x → string object ("Hello")

# Python কোনো error দেয় না
# কারণ variable শুধু reference, type না

# Internally কী হচ্ছে?

# Python internally এমনভাবে কাজ করে:    

# x → object (10)
# x → object ("Hello")

# variable শুধু pointer/reference
# object এর type আলাদা আলাদা

# Duck Typing Internally
def show(obj):
    obj.run()

# Python করে:

# দেখে obj কী type না
# শুধু দেখে run() আছে কিনা
# থাকলে execute করে
# না থাকলে → Runtime Error
# Error কখন আসে?
class A:
    pass

a = A()
a.run()

# এখানে run() নেই
# তখন error:

# AttributeError: 'A' object has no attribute 'run'

# মানে:
# Python আগে check করেনি, পরে ধরেছে

# Why Python is Dynamic?

# ✔ Runtime type resolution
# ✔ No compile-time type enforcement
# ✔ Flexible object handling
# ✔ Everything is object (int, string, function)

# Simple analogy

# Static typing → দোকানে আগে label লাগানো (int, string fixed)

# Duck typing → শুধু দেখে “এটা কাজ করছে কিনা”, label important না

# Final Summary
# Python = runtime type system
# Variable = reference to object
# Type = object-এর ভিতরে থাকে
# Method check = runtime এ হয়