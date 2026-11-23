def even_fib_upto(max_term):
	numbers = []
	x = 1
	y = 2
	new = 0
	while (x<max_term):
		if (x % 2 == 0):
			numbers.append(x)
		new = x + y
		x = y
		y = new
	return numbers

print(sum(even_fib_upto(4000000)))
