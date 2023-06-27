#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
	tracker = 0
	for m in range(x):
		try:
			print("{:d}".format(my_list[m]), end="")
		except (ValueError, TypeError):
			pass
		else:
			tracker += 1
	print()
	return (tracker)
