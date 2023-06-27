#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
	tracker = 0
	for m in range(x):
		try:
			print("{}".format(my_list[m]), end="")
		except IndexError:
			break
		else:
			tracker += 1
	print()
	return tracker
