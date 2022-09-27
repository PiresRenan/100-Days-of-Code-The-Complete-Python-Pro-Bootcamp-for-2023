# functions with arguments and output
# from pyclbr import Function


# def add(n1, n2):
#     return n1 + n2
# def subtract(n1, n2):
#     return n1 - n2
# def multiply(n1, n2):
#     return n1 * n2
# def divide(n1, n2):
#     return n1 / n2

# functions are first-class objects, can be passed around as arguments
# def calculate(calc_function, n1, n2):
#     return calc_function(n1, n2)
# result = calculate(add, 2, 3)
# print(result)

# Nested Functions
# def outer_function():
#     print("I'm outer")
#     def nested_function():
#         print("I'm inner")
#     nested_function()
# outer_function()

# Functions can be returned from other functions
# def outer_function():
#     print("I'm outer")
#     def nested_function():
#         print("I'm inner")
#     return nested_function
# inner_function = outer_function()
# inner_function()

# Python Decorator Function
from pyclbr import Function


def delay_decorator(function):
    def wrapper_function():
        sleep(2)
        # Do before the function
        function()
        function()
        # Do after the Function
    return wrapper_function
from time import sleep
@delay_decorator
def say_hello():
    print("Hello")
@delay_decorator
def say_bye():
    print("Bye")
def say_greeting():
    print("How are you? ")
say_hello()
say_bye()
say_greeting()

# Can do the decorator without the @
decorated_function = delay_decorator(say_greeting)
decorated_function()



