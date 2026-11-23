def calculate_triangle(limit):
	triangle_numbers = []
	triangle = 0
	for x in range(1, limit):
		triangle += x
		triangle_numbers.append(triangle)
	return triangle_numbers

def list_factors(triangle):
	factors = []
	for d in range(1, triangle + 1):
		if triangle % d == 0:
			factors.append(d)
	return factors

triangle_numbers = calculate_triangle(5000)

for triangle in triangle_numbers:
	factors = list_factors(triangle)
	if len(factors) > 500:
		print(triangle)
		break
	else:
		continue

