"""
Python Magic Methods (Dunder Methods) – Complete Guide
1. Object Initialization & Construction
Method	Purpose	Trigger	Example
__new__(cls, ...)	Creates a new instance	When creating object	obj = MyClass()
__init__(self, ...)	Initializes the object	After __new__	def __init__(self, name): self.name=name
__del__(self)	Destructor	When object is garbage collected	def __del__(self): print("Deleted")
2. Representation & Conversion
Method	Purpose	Trigger	Example
__str__(self)	Human-readable string	print(obj)	"Person: Alice"
__repr__(self)	Unambiguous string	repr(obj)	"Person(name='Alice')"
__format__(self, format_spec)	Format object	format(obj, spec)	"Alice".upper()
__bytes__(self)	Convert to bytes	bytes(obj)	b'Alice'
__bool__(self)	Boolean value	bool(obj)	True/False
3. Arithmetic & Numeric Operations
Method	Purpose	Trigger	Example
__add__(self, other)	+	a + b	a+b
__sub__(self, other)	-	a - b	a-b
__mul__(self, other)	*	a * b	a*b
__truediv__(self, other)	/	a / b	a/b
__floordiv__(self, other)	//	a // b	a//b
__mod__(self, other)	%	a % b	a%b
__pow__(self, other)	**	a ** b	a**b
__neg__(self)	Unary -	-a	-a
__pos__(self)	Unary +	+a	+a
__abs__(self)	abs()	abs(a)	abs(-5)
__round__(self, n)	round()	round(a, n)	round(3.1415,2)
__floor__(self)	math.floor()	math.floor(a)	3
__ceil__(self)	math.ceil()	math.ceil(a)	4
__trunc__(self)	math.trunc()	math.trunc(a)	3

There are also reflected versions (__radd__, __rsub__, etc.) for operations where your object is on the right side of the operator.

4. In-place Operations
Method	Purpose	Trigger	Example
__iadd__	+=	a += b	a += b
__isub__	-=	a -= b	a -= b
__imul__	*=	a *= b	a *= b
__itruediv__	/=	a /= b	a /= b
__ifloordiv__	//=	a //= b	a //= b
__imod__	%=	a %= b	a %= b
__ipow__	**=	a **= b	a **= b
5. Comparison Operators
Method	Purpose	Trigger	Example
__eq__	==	a == b	a==b
__ne__	!=	a != b	a!=b
__lt__	<	a < b	a<b
__le__	<=	a <= b	a<=b
__gt__	>	a > b	a>b
__ge__	>=	a >= b	a>=b
6. Container & Collection Methods
Method	Purpose	Trigger	Example
__len__	len(obj)	len(obj)	len(obj)
__getitem__	Index access	obj[key]	obj[0]
__setitem__	Assign value by index	obj[key]=value	obj[0]=10
__delitem__	Delete item	del obj[key]	del obj[0]
__iter__	Iterable	for x in obj	iter(obj)
__next__	Iterator	next(obj)	next(obj)
__contains__	in	item in obj	x in obj
__reversed__	reversed(obj)	reversed(obj)	reversed(obj)
__missing__	Missing key (dict subclass)	d[key]	Called if key not found
7. Attribute Access & Management
Method	Purpose	Trigger	Example
__getattr__	Access undefined attribute	obj.attr	called if attribute missing
__setattr__	Set attribute	obj.attr = val	obj.attr = val
__delattr__	Delete attribute	del obj.attr	del obj.attr
__getattribute__	Access any attribute	obj.attr	always called
__dir__	dir(obj)	dir(obj)	return list of attributes
8. Callable Objects
Method	Purpose	Trigger	Example
__call__	Make object callable	obj()	obj()
9. Context Managers
Method	Purpose	Trigger	Example
__enter__	Enter with block	with obj:	setup
__exit__	Exit with block	with obj:	cleanup
10. Miscellaneous
Method	Purpose	Trigger	Example
__hash__	Hash value	hash(obj)	hash(obj)
__bool__	Boolean conversion	bool(obj)	True/False
__dir__	dir()	dir(obj)	List attributes
__sizeof__	Size in memory	sys.getsizeof(obj)	sys.getsizeof(obj)
__copy__	Shallow copy	copy.copy(obj)	copy.copy(obj)
__deepcopy__	Deep copy	copy.deepcopy(obj)	copy.deepcopy(obj)
"""