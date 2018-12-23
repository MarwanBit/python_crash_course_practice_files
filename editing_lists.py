#you can append lists with the .append method
#Ex: We will add items using append in the following lines of code

family_members = ["Ismail", "Amine", "Anwar", "Aicha", "Reeses"]
print(str(family_members))
#to add people you just use the append method

family_members.append("Amine's Daughter")
family_members.append("My Daughter")
family_members.append("Anwar's Daughter")
print(str(family_members))

#using the insert method you can add items into any index in the list
#Ex:

print(str(family_members))
family_members.insert(0, "Matuda a.k.a Grandma")
print(str(family_members))

#You can use the delete command to delete items in a list
#Ex:
print(str(family_members))
del family_members[0]
print(str(family_members))
family_members.append("Matuda")
#You can remove items and keep the information for use using the pop() method
print(family_members)
popped_family_member  = family_members.pop()
print(family_members)
print(popped_family_member)
