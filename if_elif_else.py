#!/usr/bin/env python3

x = int(input("Enter an integer: "))

if x < 0:
    x = 0
    print("Neganive number changed to 0")
elif x == 0:
    print("Zero")
else:
    print("Something else")

