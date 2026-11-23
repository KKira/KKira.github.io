def is_palindrome(value):
	input = str(value)
	return (input == input[::-1])

def palindrome_generator():
	palindromes = []
	new = 0
	factor1 = 100;
	factor2 = 100;
	while ( factor1 < 1000 and factor2 < 1000):
		new = factor1 * factor2
		palindromes.append(new)
		factor1 += 1
		if (factor1 > 999):
			factor2 += 1
			factor1 = factor2
	return palindromes

print(is_palindrome(9009))
print(is_palindrome(9990))
print(max(n for n in palindrome_generator() if is_palindrome(n)))

