def factors(value):
	numbers = []
	for d in range(2, value + 1):
		while (value % d == 0):
			value = value / d
			numbers.append(d)
			if (value == 1):
				return numbers


print(factors(13195))
print(max(factors(600851475143)))
print(factors(8))
