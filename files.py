#!/usr/bin/env python3

# opens file and prints it line by line
f = open("files.py")

for line in f:
    print("{}".format(line), end="")

f.close()

# equivalent, but without the need of explicit close()
with open("files.py") as f:
    print(f.read())
# New line# New line
# New line
