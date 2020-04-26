import math
from math import pi

menu = """
Pick a shape(1-3):
   1) Square
   2) Rectangle
   3) Triangle
   4) Quit
"""
shape = int(input(menu))
while shape != 4:
   if shape == 1:
      length = float(input("Length: "))
      print( "Area of square = ", length ** 2 )
   elif shape == 2:
      length = float(input("Length: "))
      width = float(input("Width: "))
      print( "Area of rectangle = ", length * width )   

   elif shape == 3:
      area = float(input("Radius: "))
      circumference = float(input("radius: "))
      print( "Area of Circle = ", pi*radius**2 )
   shape = int(input(menu))
print(menu)
