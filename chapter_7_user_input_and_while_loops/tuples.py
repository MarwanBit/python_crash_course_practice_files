#Buffet Basic Foods

buffet_basics = ('Salad', 'Pizza', 'Steak', 'Bread', 'Chicken')
for i in buffet_basics:
	print(str(i))
	
#Now we are going to redifine buffet_basics due to it being a tuple

print('\t\nThese are the new buffet basics:')
buffet_basics = ('Sushi', 'Pizza', 'Steak', 'Bread', 'Armadillo')
for i in buffet_basics:
	print('\t\n' + str(i))
