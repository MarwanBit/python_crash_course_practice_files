# a list in python is contained with square brackets
# an example is provided in line 3
car_types = ["Ferrari","Lamborghini", "Tesl", "Nissan", "Ford", "BMW"]

#to pick an individual item in a list pick its number in the index of the list
# Ex:this would print the Lambo string cause it goes 0,1,2,3,4 and so on
print(car_types[1])
#you can then apply methods to these individual list items
print(car_types[1].upper())
#you can ask for indexes with negative numbers aswell
print(car_types[-1].upper())
#Try using the list in an operation!!
for i in car_types:
	message = "I own a" + " " + str(i)
	print(message)

print(car_types)

# you can edit lists in certain ways 
# Ex: below the item Ferrari was replaced with the string Sabel

car_types[0] = "Sabel"
print(car_types)
# You can add items to a list using the apppend method which adds the ..
# item to the end of a list 
#Ex:

car_types.append("Prius")
print(car_types[-1].title())
