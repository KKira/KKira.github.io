temporal = 0

for n in range(1000):
	if n % 3 == 0:
		temporal += n
	elif n % 5 == 0:
		temporal += n

print(temporal)
