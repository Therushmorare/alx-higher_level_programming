#!/usr/bin/python3
#Write a program that prints numbers from 0 to 99.
for num_val in range(0, 100):
    if num_val == 99:
        print("{}".format(num_val))
    else:
        print("{:02}".format(num_val), end=", ")
