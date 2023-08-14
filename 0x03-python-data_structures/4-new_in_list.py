#!/usr/bin/python3
"""Replace in a copy"""
def new_in_list(my_list, idx, element):
	if idx < 0 or idx > (len(my_list) - 1):
		return (my_list)
	"""saving the value of the ith element into saved_value"""	
	saved_value = [ith for ith in my_list]
	saved_value[idx] = element
	return (saved_value)
