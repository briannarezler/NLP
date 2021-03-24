# Lambda keyword to declare an anonymous function
# An anonymous function refers to a function declared with no name
# Lambda functions behave in the same way as regular functions that are declared using the def keyword

# A lambda function can take any number of arguments, but they
# contain only a single expression. An expression is a piece of code executed by
# the lambda function, which may or may not return any value. Lambda
# functions can be used to return function objects.

"""
remainder = lambda num: num % 2
# print(remainder(5))

product = lambda x, y: x * y
# print(product(2, 3))


def testfunc(num):
    return lambda x: x * num

result1 = testfunc(10)
restult2 = testfunc(1000)

print(result1(9))
print(restult2(9))
"""

"""
numbers_list = [2, 6, 8, 10, 11, 4, 12, 7, 13, 17, 0, 3, 21]

filtered_list = list(filter(lambda num: (num > 7), numbers_list))

print(filtered_list)
"""


# Return double of n
def addition(n):
    return n + n


# We double all numbers using regular function
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))

# Same thing using lambda
result = list(map(lambda x: x + x, numbers))
print(result)


# The same using lambda 2 variables
numbers = (1, 2, 3, 4)
numbers2 = (5, 6, 7, 8)
result = list(map(lambda x, y: x + y, numbers, numbers2))
print(result)


"""
numbers_list = [2, 6, 8, 10, 11, 4, 12, 7, 13, 17, 0, 3, 21]

mapped_list = list(map(lambda num: num % 2, numbers_list))

print(mapped_list)
"""
