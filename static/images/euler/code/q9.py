def is_pythagorean_triplet(a,b,c):
	return a**2 + b**2 == c**2

for a in range(1000):
	for b in range(a + 1, 1000):
		c = 1000 - a - b
		if is_pythagorean_triplet(a,b,c):
			print(a*b*c)
			print(a, b, c)





