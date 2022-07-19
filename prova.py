

def main():
	res = bubble_sort([6, 3, 5, 2, 7, 1])
	print('Result: ' + str(res))
	res = bubble_sort([])
	print('Result: ' + str(res))
	res = bubble_sort([5])
	print('Result: ' + str(res))

def swap_l(to_sort, ix):
	tmp = to_sort[ix + 1]
	to_sort[ix + 1] = to_sort[ix]
	to_sort[ix] = tmp

def bubble_sort(to_sort):
	if len(to_sort) <= 1:
		return to_sort
	swapped = True
	while swapped:
		swapped = False
		for ix in range(len(to_sort) - 1):
			if to_sort[ix] > to_sort[ix + 1]:
				swap_l(to_sort, ix)
				
				swapped = True				
	return to_sort

main()



