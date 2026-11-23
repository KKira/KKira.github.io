def is_prime(n):
	x = 2
	if n == x:
		return True
	while x < n:
		if n % x == 0 and n != x:
			return False
		elif n % x != 0 and n > 1:
			x += 1
		if n == x:
			return True

def prime_generator(max_term):
	primes = []
	prime_counter = 0
	x = 2
	while prime_counter < max_term:
		if is_prime(x) == True:
			primes.append(x)
			prime_counter += 1
			x += 1
		else:
			x += 1
	return primes

print(max(prime_generator(6)))
print(max(prime_generator(10001)))




