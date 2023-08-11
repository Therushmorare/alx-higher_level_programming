#!/usr/bin/python3

import sys

arguments = len(sys.argv) - 1
args = sys.argv[1:]

if arguments == 0:
    print("0 arguments.")

if arguments == 1:
    print("1 argument:")
    print("1: {}".format(args[0]))

if arguments > 1:
    print("{} arguments:".format(arguments))
    for i, arg in enumerate(args, start=1):
        print("{}: {}".format(i, arg))
