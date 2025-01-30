# LOGICAL operators and BITWISE operators

# -----Logical Operators --> and, or, not -----------(returns operand and not true/false)
# and- &&, or- ||, not- !        --> in JAVASCRIPT
# and - and, or - or, not - not  --> in Python
# checks two operators and returns one given INPUT value by deciding.
# -----------and operator--------------
# print(True and True)    - True
# print(True and False)   - False
# print(False and True)   - False
# print(False and False)  - False

# print(False and (True and True and False))  - False
# output depends on second operand if first value is truthy.
# output is first value if it is falsy. and it doesnot depend on second value.

# print(2 and 3)      -> 3
# print(3 and 2)      -> 2
# print(4 and "")     -> 
# print("" and 0)     ->
# print(-1 and -3)    -> -3
# print(0 and "")     -> 0
# print(False and 45) -> False
# print(None and 3)   -> None

# -------- or operator ----------
# output depends on second operand if first value is Falsy.
# output is first value if it is Truthy. and it doesnot depend on second value.
# print(True or False)                                  --> True
# print(False or True)                                  --> True
# print(False or (False and True))                      --> False
# print(True and (False or True and (True or False)))   --> True

# print(2 or 3)      -> 2
# print(3 or 2)      -> 3
# print("" or True)  -> True
# print(0 or 0)      -> 0
# print(0 or 1)      -> 1
# print(0 or 0 or 1) ->1

# -------- not operator -------- returns true/false
# print(not True)               -> False
# print(not False)              ->True
# print(not (True or False))    ->False
# print(not (2 or 3))           ->False
# print(not ("" and 3))         ->True


# -------  BITWISE OPERATORS----------
# and- &, or- |, xor- ^, ~, >>, << 
# convert input to binary bits and perform operation(right to left)
# leading zeros - zeros at starting , trailing zeros - zeros at the end
# performs an operation and returns a new value
# --------bitwise and ----------
# print(2 & 3) -> 2
# print(4 & 3) -> 0100 & 0011 --> 0000  => 0
# print(12 & 14) -> 1100 & 1110 --> 1100 => 12
# print(23 & 35) -> 010111 & 100011 --> 000011 => 3
# ----------bitwise or ------
# print(12 | 13)  -> 1100 | 1110 --> 1110 => 14

# ----------bitwise xor ----------
# print(12 ^ 14) --> 1100 ^ 1110 --> 0010 => 2
# print(23 ^ 35) --> 010111 ^ 100011 --> 110100 => 52

# -------left shift and right shift---------
# left shift  (Double the first value) * right value
# right shift (Half the first value and ignores decimals) * right value of halves

# print(3 << 1)  =>6 
# print(3 << 1)  =>1

# print(4 << 1) =>8
# print(4 >> 1) =>2

# print(29 << 1) => 58
# print(29 >> 1) => 14


# 0011 - left shift - 0110
# 0011 - right shift- 0001

# 001011(11) - right shift - 000101(5)
# 001011(11) - left shift  - 010110(22)

# ----------negation( ~ ) -----------
# add one to input and negate it





