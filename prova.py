

def main():
	res = bubble_sort([6, 3, 5, 2, 7, 1])
	# res = bubble_sort([])
	# res = bubble_sort([5])
	print('Result: ' + str(res))


def bubble_sort(to_sort):
	if len(to_sort) <= 1:
		return to_sort
	swapped = True
	while swapped:
		swapped = False
		for ix in range(len(to_sort) - 1):
			if to_sort[ix] > to_sort[ix + 1]:
				tmp = to_sort[ix + 1]
				to_sort[ix + 1] = to_sort[ix]
				to_sort[ix] = tmp
				swapped = True				
	return to_sort

main()



