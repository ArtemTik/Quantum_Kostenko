N = int(input("Please enter a number: "))
summ = 0
for i in range(1, N + 1):
	summ = summ + i
	if N > 10**25:
		break
print("Sum of first", i, "numbers is: ", summ)
