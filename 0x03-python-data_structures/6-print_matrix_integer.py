#!/usr/bin/python3
""" Lists of lists = Matrix"""
def print_matrix_integer(matrix=[[]]):
	""" just like in c i = rows, j = columns"""
	for i in matrix:
		for j in i:
			print("{:d}".format(j), end=" " if j != i[-1] else "")
			print()
