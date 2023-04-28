# import math
# from firstClass import my_function
# import numpy as np
# from Generator import RandomGenerator

# import random

# # Inicjalizacja generatora losowego LCG0 ziarnem
# random.seed(1, version=1)

# # Generowanie 10 liczb losowych z przedziału [0, 1)
# for i in range(10):
#     print(random.random())


# np.array([1,2,3])

# # msg = "Hello świecie"
# # print(msg)

# # my_function()

# print(RandomGenerator(1))
from .Process import *
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def product(a,b):
    return a*b
def quotient(a,b):
    return a/b
print("The addition of two numbers are:",add(9,4))
