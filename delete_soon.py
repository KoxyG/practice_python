#!/usr/bin/python3
print_list_integer = __import__('0-print_list_integer').print_list_integer

my_list = [1, 2, 3, 4, 5]
print_list_integer(my_list)


def print_list_integer(my_list=[]):
    for x in range (1, 5):
        if x > 1:
            print("{}".format(x))