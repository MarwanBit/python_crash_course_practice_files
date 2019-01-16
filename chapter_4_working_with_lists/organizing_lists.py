places_to_visit = ['Spain', 'California', 'Venice', 'Egyptian Pyramids', 'Niagra Falls']

#Below is the original order of the following list
print(places_to_visit)

#Below is the same list but sorted
print(sorted(places_to_visit))

#The list is still in the original order though because of the nature of the sorted function
print(places_to_visit)

#Now lets try to temporarily print the list in reverse alphabetical order
places_to_visit.reverse()
print(places_to_visit)

#Now lets try to sort the list
places_to_visit.sort()
print(places_to_visit)

#Now lets sort it in reversed alphabetical order
places_to_visit.sort(reverse=True)
print(places_to_visit)
