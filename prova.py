

def main():
	my_array = [6, 3, 5, 2, 7, 1]
	print('Input: ' + str(my_array))
	bubble_sort(my_array)
	print('Result: ' + str(my_array))
	my_array = []
	print('Input: ' + str(my_array))
	bubble_sort(my_array)
	print('Result: ' + str(my_array))
	my_array = [6]
	print('Input: ' + str(my_array))
	bubble_sort(my_array)
	print('Result: ' + str(my_array))

def swap_l(to_sort, ix):
	tmp = to_sort[ix + 1]
	to_sort[ix + 1] = to_sort[ix]
	to_sort[ix] = tmp

def bubble_sort(to_sort):
	n = len(to_sort)
	if n <= 1:
		return to_sort
	swapped = True
	for i in range(n):
		swapped = False
		for j in range(n - i - 1):
			if to_sort[j] > to_sort[j + 1]:
				swap_l(to_sort, j)
				swapped = True

main()
