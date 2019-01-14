import car_class
from car_class import *
from car_class import Car, ElectricCar

my_tesla = ElectricCar("80%", "20Kwh", "Tesla", "2018", "400", "Tesla X")
my_tesla.car_description()
my_tesla.read_odometer()
my_tesla.increment_odometer(14)
my_tesla.get_charge()