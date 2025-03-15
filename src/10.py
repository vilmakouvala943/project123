import random 
from math import sqrt 
def calculate_area(radius): 
 return pi * radius ** 2 
def calculate_circumference(radius): 
 return 2 * pi * radius 
def main(): 
 radius = float(input("Enter the value of radius: ")) 
 area = calculate_area(radius) 
 circumference = calculate_circumference(radius) 
 print("The area is", area) 
 print("The circumference is", circumference) 
 if __name__ == "__main__": 
 main()