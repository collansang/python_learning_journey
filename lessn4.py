#arithmetic operators (math functions)
from doctest import run_docstring_examples

friends = 10
#friends = friends + 1
#friends += 1
#friends -= 1
#friends *= 3
#friends /=2
#friends = friends **2
#friends **= 2
#remainder = friends % 3


#print(remainder)


# x =3.14
# y = 4
# z = 7
#result = round(x)  # rounds off the number to the nearest whole number.
#print(result)

# f = -4
#result = abs(y)   #Cnverts a negative to a positive integer.
#print(result)
#result = pow(f, 3) #power
#(result)

#result = max(x,y,z)  #selects the maximum value among the numbers.
#print(result)
#result = min(x,y,z)  #selects the minimum value amng the numbers
#print(result)


#import math
# w = 25
# print(math.pi)   #pi constant in math
# print(math.e)    # constant in physics
# result = math.sqrt(w)  # square root
# print(result)


# x = 9.1
# result = math.ceil(x)   #(converts t the next whole number)
# print(result)
#
# d = 5.9
# result = math.floor(d) # converts to next smallest number
# print(result)


#sample exercises
#circumference of a circle c= 2pi r
# import math
# radius = float(input("Enter the readius of the circle: "))
# circumference = 2 *math.pi * (radius)
# print(f"The circumference of the circle is {round(circumference, 2)} cm")
#

# #area of the circle
# import math
# radius = float(input("Enter the radius of the circle:"))
# area = math.pi  * pow(radius,2)
# print(f"The area of the circle {round(area, 2)} cm^2")
#


#hypotenuse f the right angle triangle
import math
height = float(input("Enter the height of the triangle in cm:"))
base = float(input("Enter the base of the triangle in cm:"))
hypotenuse = math.sqrt((height) ** 2 + (base) **2)
print(f" The hypotenuse of the triangle is {hypotenuse} cm")
