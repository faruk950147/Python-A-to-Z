# =========================== Operator Precedence and Associativity ===========================
# operator precedence and associativity
# Operator Precedence is the order in which operators are evaluated.
# Operator Associativity is the order in which operators are evaluated.

# Operator Associativity
# Left to Right
# Right to Left

# Operator Precedence in Python (Highest to Lowest)
# Precedence	Operators	Description
# 1	()	# Parentheses
# 2	**	# Exponentiation
# 3	+x, -x, ~x	# Unary operators (positive, negation, bitwise NOT)
# 4	*, /, //, %	# Multiplication, Division, Floor Div, Modulo
# 5	+, -	# Addition, Subtraction
# 6	<<, >>	# Bitwise Shift
# 7	&	# Bitwise AND
# 8	^	# Bitwise XOR
# 9	`	`
# 10	==, !=, >, >=, <, <=	# Comparisons
# 11	not	# Logical NOT
# 12	and	# Logical AND
# 13	or	# Logical OR
# 14	=, +=, -=, *=, ...	# Assignment (lowest precedence)

# Operator Associativity
# Most operators	Left to Right
# **, unary +, -	Right to Left

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