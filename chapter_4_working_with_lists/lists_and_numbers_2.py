print("\tHere is the list of odd numbers from 1-20")

for numbers in range(1,21,2):
	print(numbers)

print("\tNow for the list of threes.......")

for numbers in range(3,31,3):
	print(numbers)

print("\tNow its time for the cubed numbers!")

cubed_number_combos = []
for numbers in range(1,11):
	cubed_number_combos.append(numbers**3)
	print(numbers**3)
	
print(cubed_number_combos)
	
print("\tNow is time for the list comprehension, check the code to see")	
	
cubed_number_combos_2 = [value**3 for value in range(1,11)]
print(cubed_number_combos_2)
