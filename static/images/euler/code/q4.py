def palindrome(value):
	i = 0
	input = str(value)
	temp = []
	for d in input:
		temp.append(d)
	if ( len(temp) == 1):
		return temp
	else:
		j = len(temp)
	while(temp[i] == temp[j-1]):
		i += 1
		j -= 1
		if (i >= j):
			return True

def highest_factor(absolute_factor):
	variable_factor = absolute_factor
	new = absolute_factor * variable_factor
	while( palindrome(new) == None and variable_factor > 99):
		variable_factor -= 1
		new = absolute_factor * variable_factor
		if (palindrome(new) == None and variable_factor == 99):
			absolute_factor -= 1
			variable_factor = absolute_factor
		elif (palindrome(new) == True):
			return variable_factor, absolute_factor

print(highest_factor(999))
