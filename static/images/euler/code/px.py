# numbers = []

# for x in range(1000):
# 	if x % 3 == 0 or x % 5 == 0:
# 		numbers.append(x)

# print(sum(numbers))

# number = 600851475143
# prime_factors = []
# x = 2

# while number > 1:
# 	if number % x == 0:
# 			number /= x
# 			prime_factors.append(x)
# 	else:
# 		x += 1

# print(prime_factors)

# def is_palindrome(x):
# 	number = str(x)
# 	return number == number[::-1]

# def three_d_product():
# 	products = []
# 	three_d_number = range(100,1000)

# 	for x in three_d_number:
# 		for y in three_d_number:
# 			product = x * y
# 			if is_palindrome(product) == True:
# 				products.append(product)

# 	return products



# print(is_palindrome(9009))
# print(max(three_d_product()))

# def evenly_divisible(number, limit):
	
# 	for x in range(2, limit + 1):
# 		if number % x != 0:
# 			return False
# 	return True

# number = 2
# while not evenly_divisible(number, 20):
# 	number += 1
# print(number)

# sum_squares = 0
# running_sum = 0


# for x in range(101):
# 	sum_squares += x*x
# 	running_sum += x

# print(running_sum**2 - sum_squares)

def siev_list(limit):
	is_prime = []
	prime_list = []
	x = 1

	while x < limit + 1:
		is_prime.append(1)
		x += 1

	is_prime[0] = 0
	is_prime[1] = 0

	for x in range(limit):
		if is_prime[x] == 1:
			prime_list.append(x)
			for y in range(x *2, len(is_prime), x):
				is_prime[y] = 0

	return prime_list



print(siev_list(300000)[10000])



