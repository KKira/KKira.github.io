def multiples(value):
	temporal = 0
	for n in range(value):
		if (n % 3 == 0):
			temporal += n
		elif (n % 7 == 0):
			temporal += n
	return temporal


print(multiples(500))
