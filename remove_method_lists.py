# you can remove items based off of there value on lists 

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)

too_expensive = 'ducati'
motorcycles.append('ducati')
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + str(too_expensive.title()) + " is too expensive for me.")
