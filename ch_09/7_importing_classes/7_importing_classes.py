# IMPORTING CLASSES



#from car import Car
#from car import ElectricCar
#from car import Car, ElectricCar
#from car import *

from car import Car
from electric_car import ElectricCar as EC

my_new_car = Car("audi", "a4", 2024)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()
print()

my_leaf = EC("nisan", "leaf", 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()
print()



'''
import car

my_mustang = car.Car("ford", "mustang", 2024)
print(my_mustang.get_descriptive_name())

my_leaf = car.ElectricCar("nissan", "leaf", 2024)
print(my_leaf.get_descriptive_name())
'''

'''
import car as c
my_mustang = c.Car("ford", "mustang", 2024)
print(my_mustang.get_descriptive_name())
print()
'''
