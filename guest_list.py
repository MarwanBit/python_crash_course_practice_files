guest_list = ['Logic', 'Kendrick Lamar', 'J. Cole', 'Tai Lopez', 'Bernie Sanders']

for i in guest_list:
	print("\nHello," + "\nThis is Marwan Bit and I was wondering if you," + " " + str(i) + " " + "would like to come to my party")

guest_who_cant_come = guest_list[4]
print("\nSorry to everyone but" + " " + str(guest_who_cant_come) + " can't make it")

guest_list.remove('Bernie Sanders')
print("\nThe new guest list now includes," + "\n" + str(guest_list))

print("\n\tNow here are the updated invitations")
for i in guest_list:
	print("\nHello," + "\nThis is Marwan Bit again, and I was wondering if you," + " " + str(i) + " " + "would still like to come to my party")
	

print("\n\tOhh! we found a bigger table!")
guest_list.insert(4, 'Thomas Frank')
guest_list.insert(0, 'Joe Rogan')
print("This is the new list," + " " + str(guest_list))
print("\tOh Wait there's one more guest")
guest_list.append('Mr. Jackson')

print("\tSorry the new table won't arrive in time therefore I can only invite two people")
number_of_canceled_guests = int(5)

while number_of_canceled_guests > 0:
	removed_guest = guest_list.pop()
	print("\nHello," + "\nThis is Marwan Bit and I can't fit you ," + " " + str(removed_guest) + " " + "in the table so sadly I can't invite you")
	number_of_canceled_guests = int(number_of_canceled_guests) - 1 
	
for i in guest_list:
	print("\n\tI am inviting" + " " + str(len(guest_list)) + " people to my party")
	print("\nHello," + " " + str(i) + " I am happy to say that you can make it to my party")

del guest_list[0]
guest_list.remove('Logic')
print(str(guest_list))
