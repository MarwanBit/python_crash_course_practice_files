class Car():

	def __init__(self, manufacturer, year, mileage, brand):
		self.manufacturer = str(manufacturer)
		self.year = str(year)
		self.mileage = str(mileage)
		self.brand = str(brand)
		self.odometer = int(mileage)

	def car_description(self):
		print(
			"The car is a " + str(self.year) + " " +
			str(self.brand) +'.' + '\nIt is manufactured by ' +
			str(self.manufacturer) + " and it has " +
			str(self.mileage) + " miles."
			)

	def read_odometer(self):
		print(
			"Your " + str(self.brand) +
			" has " + str(self.odometer) +
			" miles!"
			)

	def increment_odometer(self, miles_to_be_added):
		self.odometer += int(miles_to_be_added)
		print(
			"Your " + str(self.brand) +
			" Has traveled another " +
			str(miles_to_be_added) +
			" miles."
			)
		print(
			"\nResulting in a total of..." +
			str(self.odometer) + " miles."
			)

class ElectricCar(Car):

	def __init__(self, charge, size_of_battery, manufacturer, year, mileage, brand):
		super().__init__(manufacturer, year, mileage, brand)
		self.charge = charge
		self.size_of_battery = size_of_battery

	def get_charge(self):
		print(
			"Your car's charge is.." +
			str(self.charge)
			)
	def get_size_of_battery(self):
		print(
			"The size of your battery is..." +
			str(self.size_of_battery)
			)