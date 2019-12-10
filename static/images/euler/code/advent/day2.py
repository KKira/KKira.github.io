def readfile():
	with open("day2.txt") as fp:
		contents = fp.read().strip()
		all_rows = []
		for row in contents.split('\n'):
			all_rows.append([int(numbers) for numbers in row.split('x')])
		return all_rows

gifts_dimension = readfile()
total_paper = 0

for l, w, h in gifts_dimension:
	areas = [l*w, w*h, h*l]
	total_paper += sum(areas) * 2
	total_paper += min(areas)


print(total_paper)

ribbon = 0

for l, w, h in gifts_dimension:
	perimeters = [2*(l + w), 2*(l+h), 2*(h+w)]
	ribbon += min(perimeters)
	ribbon += l*w*h

print(ribbon)