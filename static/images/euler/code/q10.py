#summation of primes below 2 million

def prime_sieve(limit):
	is_prime = [1 for x in range(limit + 1)]
	primes = []		

	is_prime[0] = 0
	is_prime[1] = 0

	for x in range(limit + 1):
		if is_prime[x]:
			primes.append(x)
			for y in range(x *2, limit +1, x):
				is_prime[y] = 0

	return primes

print(sum(prime_sieve(2000000)))

