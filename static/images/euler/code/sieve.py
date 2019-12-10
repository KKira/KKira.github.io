def list_siev(max_term):
	is_prime = []
	primes = []
	for x in range(max_term + 1):
			is_prime.append(1)
	is_prime[0] = 0
	is_prime[1] = 0
	for y in range(2, max_term + 1):
		for x in range(y *2, max_term + 1, y):
			is_prime[x] = 0

	for x in range(max_term + 1):
		if is_prime[x] == 1:
			primes.append(x)

	return primes


print(list_siev(300000)[10001]) 

