count = 0

for i in range(3,118):
	if i % 3 == 0 and i % 5 == 0:
		count = count + 15
	elif i % 3 == 0:
		count = count + 3
	elif i % 5 == 0:
		count = count + 5
	else:
		count = count + 1

print count
