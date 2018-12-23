favorite_pizzas = ['Cheese', 'Mushroom', 'Black Olive', 'Chicken', 'Stuffed Crust']
for pizza_types in favorite_pizzas:
	print('I love' + " " + str(pizza_types) + " pizza.")

print('The first three items in the favorite pizzas list are...')
print(favorite_pizzas[0:3])

print('Three items from the middle of the list are....')
print(favorite_pizzas[1:4])

print('The last three items of the list are....')
print(favorite_pizzas[2:5])

friends_pizzas = favorite_pizzas[:]
friends_pizzas.append('Turkish')

print('My favorite pizzzas are....')
print(favorite_pizzas)

print('My friends favorite pizzas are....')
print(friends_pizzas)

print("I love pizza so much. I love cheese, mushroom, black olive, chicken, stuffed crust and even more types of pizza.")
print("I love pizza so much its my guilty food!")

animals_with_similarities = ['Dog', 'Cat', 'Wolve', 'Tiger', 'Lion', 'Chupacabra',]
for animal in animals_with_similarities:
	print("A" + " " + str(animal) + " would make an amazing pet.")
	
print("All these animals are great because all of them are furry and fourlegged!")


