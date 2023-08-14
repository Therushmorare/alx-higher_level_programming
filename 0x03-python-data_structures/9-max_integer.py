#!/usr/bin/python3
"""Find the max"""
def max_integer(my_list=[]):
	if len(my_list) == 0:
		return (None)
	"""just like sortiing take the first index as starting point"""
	largest_element = my_list[0]

	for i in range(len(my_list)):
		"""compare all llist values to starting point"""
		if my_list[i] > largest_element:
			""" feed starting point largest value found in list"""
			largest_element = my_list[i]
	return (largest_element)
