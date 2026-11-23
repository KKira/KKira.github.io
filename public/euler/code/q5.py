# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

def is_evenly_divisible(value):
	n = 1
	while (value % n == 0):
			n += 1
			if (n > 20):
				return True

def first_divisible():
	values = []
	x = 1
	while (is_evenly_divisible(x) == None):
		x += 1
		if (is_evenly_divisible(x) == True):
			values.append(x)
			return values

print(is_evenly_divisible(2520))
# print(first_divisible())
print(is_evenly_divisible(232792560))


# print(min(n for n in value_generator() if is_evenly_divisible(n)))

# # What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?