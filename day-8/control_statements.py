# Control Staatements - Controls flow of Execution of code
# Conditional Statements, Loops and Jump Statements

# Indentation - to start a line of writing further from the left-hand side of the page than the other lines

# --------------Conditional Statements(if, else, elif) ----------------------
# "Else" statement cannot be written without "if" statement

# Logical error  : code runs but wrong output
# Syntax error : code doesnt runs and no output is displayed


# num=int(input("Enter the number : "))
# if num>0:
#     print("positive")
# else:
#     print("zero or negative")
# -------Nested Conditional statements-----------
# conditional statements inside another conditional statements
# if num>0:
#     print("Positive")
# else:
#     if num==0:
#         print("zero")
#     else: 
#         print("Negative")

# if num>0:
#     if num==1:
#         print("one")
#     else:
#         print("Positive")
# else:
#     if num==0:
#         print("zero")
#     else: 
#         print("Negative")

# if num>0:
#     print("Positive")
# elif num == 0:
#     print("zero")
# elif num == -1:
#     print("minus 1")
# elif num == -2:
#     print("minus 2")
# else:
#     print("Negative")
# -------  method-1  ------
# if num==1:
#     print("one")
# elif num>0:
#     print("Positive")
# elif num == 0:
#     print("zero")
# elif num == -1:
#     print("minus 1")
# elif num == -2:
#     print("minus 2")
# else:
#     print("Negative")
# -------  method-2  ------
# if num>0 and num != 1:
#     print("Positive")
# elif num==1:
#     print("one")
# elif num == 0:
#     print("zero")
# elif num == -1:
#     print("minus 1")
# elif num == -2:
#     print("minus 2")
# else:
#     print("Negative")
# -------  method-3  ------
# if num>0:
#     if num==1:
#         print("One")
#     else:
#         print("Positive")
# elif num == 0:
#     print("zero")
# elif num == -1:
#     print("minus 1")
# elif num == -2:
#     print("minus 2")
# else:
#     print("Negative")

# ----------- Current bill calculation --------------
# 100 units - per unit 50 rupees
# 101 to 200 - per unit 100 rupees
# 201 to 300 - per unit 150 rupees
#          without elif
# unit=int(input("enter the number of units : "))
# if unit>0:
#     if unit<=100:
#         print(unit*50)
#     else:
#         if unit<=200:
#             print(unit*100)
#         else:
#             print(unit*150)
# else:
#     print("Invalid")

# if unit<101:
#     print(unit*50)
# else:
#     if unit<201:
#         print(unit*100)
#     else:
#         print(unit*150)

# if unit<=50:
#     print("zero bill")
# else:
#     if unit<101:
#         print(unit*50)
#     else:
#         if unit<201:
#             print(unit*100)
#         else:
#             print(unit*150)


# -------------------  LOOPS  ------------------------------
# used for repetation of same task
# time, money, Efficiency, Readable, less code, file space, maintainability

# for loop, while loop


# for i in range(1,1000):
#     print("sorry")





