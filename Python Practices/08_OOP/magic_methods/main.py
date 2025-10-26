import copy

class Container:
    def __init__(self, name, items):
        self.name = name
        self.items = list(items)
        self.index = 0
        print(f"Container '{self.name}' created!")

    # ----------------- Representation -----------------
    def __str__(self):
        return f"MyContainer '{self.name}' with items: {self.items}"

    def __repr__(self):
        return f"MyContainer(name={self.name!r}, items={self.items!r})"

    def __bytes__(self):
        return str(self.items).encode()

    def __format__(self, spec):
        return f"{self.name.upper()} [{len(self.items)} items]"

    def __len__(self):
        return len(self.items)

    def __bool__(self):
        return bool(self.items)

    # ----------------- Item Access -----------------
    def __getitem__(self, key):
        return self.items[key]

    def __setitem__(self, key, value):
        self.items[key] = value

    def __delitem__(self, key):
        del self.items[key]

    def __contains__(self, value):
        return value in self.items

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self.items):
            raise StopIteration
        val = self.items[self.index]
        self.index += 1
        return val

    def __reversed__(self):
        return reversed(self.items)

    # ----------------- Attribute Access -----------------
    def __getattr__(self, attr):
        return f"'{attr}' not found!"

    def __setattr__(self, attr, value):
        super().__setattr__(attr, value)

    def __delattr__(self, attr):
        super().__delattr__(attr)

    def __dir__(self):
        return list(self.__dict__.keys()) + ["custom_method"]

    # ----------------- Arithmetic -----------------
    def __add__(self, other):
        if isinstance(other, MyContainer):
            return MyContainer(self.name + "&" + other.name, self.items + other.items)
        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, MyContainer):
            self.items += other.items
        return self

    # ----------------- Callables -----------------
    def __call__(self, times=1):
        return self.items * times

    # ----------------- Context Manager -----------------
    def __enter__(self):
        print(f"Entering context for {self.name}")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print(f"Exiting context for {self.name}")
        if exc_type:
            print(f"Exception: {exc_type}, {exc_value}")
        return True  # suppress exceptions

    # ----------------- Copying -----------------
    def __copy__(self):
        return MyContainer(self.name + "_copy", self.items.copy())

    def __deepcopy__(self, memo):
        return MyContainer(self.name + "_deepcopy", copy.deepcopy(self.items, memo))

    # ----------------- Destructor -----------------
    def __del__(self):
        print(f"Container '{self.name}' deleted!")

# ====================== Testing ======================
c1 = Container("Alpha", [1,2,3])
print(c1)                     # __str__
print(repr(c1))               # __repr__
print(bytes(c1))              # __bytes__
print(format(c1))             # __format__
print(len(c1))                # __len__
print(bool(c1))               # __bool__

print(c1[0])                  # __getitem__
c1[0] = 100                   # __setitem__
del c1[1]                      # __delitem__
print(2 in c1)                 # __contains__

for x in c1:                   # __iter__ + __next__
    print(x)

print(list(reversed(c1)))      # __reversed__

print(c1.unknown)              # __getattr__
c1.new_attr = "Hello"          # __setattr__
del c1.new_attr                 # __delattr__
print(dir(c1))                 # __dir__

c2 = MyContainer("Beta", [4,5])
c3 = c1 + c2                    # __add__
print(c3)

c1 += c2                        # __iadd__
print(c1)

print(c1(2))                     # __call__

with c1 as container:           # __enter__ + __exit__
    print("Inside with block")

c_copy = copy.copy(c1)          # __copy__
c_deep = copy.deepcopy(c1)      # __deepcopy__

del c1                          # __del__
del c2
del c3
del c_copy
del c_deep
