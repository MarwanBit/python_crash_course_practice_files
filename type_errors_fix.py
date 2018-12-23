
#the chunk of code below causes an error to combining to trying to ...
#combine two different data types

age = 23
message = "Happy" + age + "rd Birthday"
print(message)

#to fix this you make the data types consistent between the operations

age = 23
message = "Happy" + str(age) + "rd Birthday"
print(message)
