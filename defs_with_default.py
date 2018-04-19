#!/usr/bin/env python3

def phrase_builder(first="Lol", sec="Troll", third="Ololo"):
    print("Hello, hello: you are {}, {}, {}".format(first, sec, third))

phrase_builder() # with all defaults
phrase_builder("Eggs", "Spam", "Yum") # works
phrase_builder("Eggs", "Spam") # also works
phrase_builder("Eggs", "Spam", third="Yum") # also works
# phrase_builder("Eggs", sec="Spam", "Yum") # doesn't work
