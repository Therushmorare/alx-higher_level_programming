#!/usr/bin/python3
"""Only by 2"""
def divisible_by_2(my_list=[]):
    elements_divisible = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            elements_divisible.append(True)
        else:
            elements_divisible.append(False)

    return (elements_divisible)
