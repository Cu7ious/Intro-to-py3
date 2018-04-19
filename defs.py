#!/usr/bin/env python3


def function():
    """
        Demonstrates that functions in Python
        always return something
    """

    print("Function named `function` was called")


print("Return value of the `function` is: {}".format(function()))


def add (a, b):
    """
        Demonstrates the scope of the variables
        In Python parameters are variables with the local scope.
        Vars `a` & `b` here have nothing in common with the vars
        outside of the function.
    """
    return (a + b)

a = 2
b = 4

print("{} + {} = {}".format(a, b, add(a, b)))
