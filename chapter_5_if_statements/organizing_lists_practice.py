favorite_rappers = ['Kendrick Lamar', 'Vince Staples', 'Big K.R.I.T', 'Logic', 'J. Cole', 'Tyler, The Creator',]
print(favorite_rappers)
print(favorite_rappers[0])
print(favorite_rappers[-1])

print("The first rapper I ever listened to was," + " " + favorite_rappers[3] + ".")

print(favorite_rappers)
favorite_rappers[0] = 'Kendrick Llama'
print(favorite_rappers)

favorite_rappers.append('Noname')
print(favorite_rappers)

favorite_rappers.insert(0, 'Big Sean')
print(favorite_rappers)

del favorite_rappers[0]
print(favorite_rappers)

popped_favorite_rapper = favorite_rappers.pop()
print(popped_favorite_rapper)
print(favorite_rappers)

least_favorite_rapper = favorite_rappers.pop(2)
print(least_favorite_rapper)

favorite_rappers.remove('Vince Staples')
print(favorite_rappers)

favorite_rappers.sort()
print(favorite_rappers)

favorite_rappers.sort(reverse=True)
print(favorite_rappers)

favorite_rappers = ['Kendrick Lamar', 'Vince Staples', 'Big K.R.I.T', 'Logic', 'J. Cole', 'Tyler, The Creator',]
print(favorite_rappers)
print(sorted(favorite_rappers))
print(favorite_rappers)

favorite_rappers.reverse()
print(favorite_rappers)

print(len(favorite_rappers))
