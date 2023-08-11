#!/usr/bin/python3

if __name__ == "__main__":
	""" print some of args"""
	import sys

	end_value = []
	arguments = sys.argv[1:]

	for arg in arguments:
		end_value.append(int(arg))

	final_val = sum(end_value)

	print(final_val)
