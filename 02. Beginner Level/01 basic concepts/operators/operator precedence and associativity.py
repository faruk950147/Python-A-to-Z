# =========================== Operator Precedence and Associativity ===========================
'''
operator precedence and associativity
Operator Precedence is the order in which operators are evaluated.
Operator Associativity is the order in which operators are evaluated.

Operator Associativity
Left to Right
Right to Left

1. Operator Precedence
Precedence নির্ধারণ করে কোন operator আগে execute হবে।
যার precedence বেশি, সেটি আগে evaluate হবে।

Example
x = 5 + 3 * 2

এখানে * এর precedence + থেকে বেশি।
তাই আগে হবে:

3 * 2 = 6
তারপর:
5 + 6 = 11
Result:
x = 11

2. Associativity
যখন দুইটি operator-এর precedence একই হয়, তখন কোন দিক থেকে evaluate হবে তা 
Associativity নির্ধারণ করে।

Left to Right Associativity
10 - 5 - 2
- operator একই precedence এর।
তাই left → right evaluate হবে:
10 - 5 = 5
5 - 2 = 3
Result:
3
Right to Left Associativity
2 ** 3 ** 2

** operator right → left associative।

তাই:

3 ** 2 = 9
2 ** 9 = 512

Result:
512

Common Operator Precedence Table (High → Low)
Precedence	Operators	Associativity
Highest	()	Left to Right 1st priority
	**	Right to Left 2nd priority
	* / // %	Left to Right 3rd priority
	+ -	Left to Right 4th priority
	== != > < >= <=	Left to Right 5th priority
	and	Left to Right 6th priority
Lowest	or	Left to Right 7th priority

Example Combined
result = 10 + 2 * 3 ** 2

Step-by-step:

3 ** 2 = 9
2 * 9 = 18
10 + 18 = 28

Result:

28
Parentheses () Priority

Parentheses সবসময় highest priority পায়।

(10 + 2) * 3

আগে:

10 + 2 = 12
তারপর:
12 * 3 = 36
Important Points
Precedence বলে কোন operator আগে চলবে
Associativity বলে কোন direction থেকে চলবে
() ব্যবহার করলে confusion কমে
Short Formula
Precedence → Priority
Associativity → Direction
'''

result = 3 + 4 * 2
# Output: 11, because 4*2 is done first, then +3

result = (3 + 4) * 2
# Output: 14, because parentheses override precedence

result = 2 ** 3 ** 2
# Output: 512, because it's 2 ** (3 ** 2), due to right-to-left associativity of **

result = -3 ** 2
# Output: -9, because it's interpreted as -(3 ** 2), not (-3) ** 2

# Rule of Thumb

# Use parentheses () to make your code readable and unambiguous.

# Remember that exponentiation ** is right-associative, while most other operators are left-associative.

# Multiplication/division comes before addition/subtraction.