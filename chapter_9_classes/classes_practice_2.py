class Restaurant():
	'''
	This class is used to create a specific restaurant
	with a name, cuisine type and the methods to describe and
	declare the restaurant open or not
	'''
	   
	def __init__(self, restaurant_name, cuisine_type):
		'''
		This init method stores the variables restaurant_name and cuisine
		type for further use in other methods defined in this class 
		'''
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0
		
	def describe_restaurant(self):
		print("\n\tThe name of the restaurant is.. " + str(self.restaurant_name.title()))
		print("\n\tThis restaurant specializes in.. " + str(self.cuisine_type.title()))
		print("\n\tThis restaurant has served.. " + str(self.number_served) + " people.")
		
	def open_restaurant(self):
		print("\n " + str(self.restaurant_name) + " is open!!")
		
	def set_number_served(self, set_number_served_int):
		self.number_served = int(set_number_served_int)
		print("\nThe number of people served has been updated to.. " + str(self.number_served))
		
	def increment_number_served(self, increment_set_number_served_int, duration_length):
		self.number_served += int(increment_set_number_served_int)
		print(
			"\t\t" +
			str(increment_set_number_served_int) + 
			" people has been served in the duration of..." +
			str(duration_length) +
			".\n\t\tThe total amount of people served that have been served..." +
			str(self.number_served)
			)
		
class IceCreamStand(Restaurant):
	'''
	This class is a subclass of Restaurant, it deals with 
	ice cream specific methods which are only available to
	the IiceCreamStand Subclass!
	'''
	
	def __init__(self, restaurant_name, cuisine_type):
		super().__init__(restaurant_name, cuisine_type)
		self.flavor_of_the_day = ""
		self.ice_cream_flavors = []
		
	def display_ice_cream_stand_flavors(self, *flavors):
		print(
				"\nThese are the flavors of icecream available..." +
				"\n\t" 
			)
		print(flavors)
			
my_ice_cream_stand = IceCreamStand("Kelly's Ice Cream", "Ice Cream")
my_ice_cream_stand.describe_restaurant()
my_ice_cream_stand.display_ice_cream_stand_flavors("Blueberry", "Chocolate", "Strawberry")
				
	
