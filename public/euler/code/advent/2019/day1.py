def readfile():
	with open("day1.txt") as fp:
		contents = fp.read().strip()
		all_rows = []
		for row in contents.split('\n'):
			all_rows.append(int(row))
		return all_rows

instructions = readfile()
total_fuel = 0

for module_mass in instructions:
	fuel = int(module_mass/3) - 2
	total_fuel += fuel
	while fuel > 0:
		fuel = int(fuel/3) - 2
		if fuel < 0:
			continue
		else:
			total_fuel += fuel

print(total_fuel)