#!/usr/bin/python3
# 100-print_tebahpl.py
i_th_val = 0
for char in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(char - i_th_val)), end="")
    i_th_val = 32 if i_th_val == 0 else 0
