
family_members = ["Ismail", "Me", "Amine", "Anwar", "Aicha"]

print(family_members)
popped_family_member  = family_members.pop()
print(family_members)
print(popped_family_member)

print("Ohh No were did" + " " + str(popped_family_member.title()) + " " + "GO?")

#You can also pop items based off of there index

print(family_members)
popped_family_member_2 = family_members.pop(1)
print(family_members)
print(popped_family_member_2.upper())
print("Ohh No were did" + " " + str(popped_family_member_2.upper()) + " " + "GO?")

