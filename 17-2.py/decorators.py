# Decorators :
# ->  single decprator can be used for many other functions.
# ->  addons to already having entity or function
# ->  decorators are also functions
# ->  creates a new function and returns it.....
# ->  accepts a function as a parameter or argument

# when we call printer function , wrapper function gets called and in that printer function in it (func()) will be called.

def example_decorator(func):
    def wrapper(a,b):
        print("check a4 sheets.....")
        print("check cartridge....")
        func(a,b)
        print("Thank You.....")
    
    return wrapper

# @example_decorator
# def printer():
#     print("printing in progress.......")

# printer()

@example_decorator
def sum(a,b):
    print(a + b)

sum(10, 20)
a = 10
b = 20
sum(a,b)

# Problem Solving 
# why -> a metric for software world to shortlist candidates
# #   -> to solve bugs and features after joining a job

# 3 things for PS (33% each)
# 1.Undertsand the question carefully
# 2.Algorithm
# 3.How to code it in a programming language
# BONUS - Edge cases(write all exceptions)******
# Code Quality (naming conventions,use functions, use comments)


# PREREQUISITS FOR PROBLEM SOLVING
# how to declare diff types of data types
# conditional statements - if and else , elif
# loops - for and while, jump statements - break, continue 
# functions - Declaration and calling , uses of return statement
# Inbuilt functions - alteast the most famous omes - string and list

# week 1 -> if else and loops
# week 2 -> list manipulations + searching and sortong
# week 3 -> string manipulations + patterns
# week 4 -> dictionary problems
