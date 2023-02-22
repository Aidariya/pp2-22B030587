import math 
n = int(input("Input number of sides: "))
l = int(input("Input the length of a side: "))
x = l**2 * n / (4 * math.tan(math.pi/n))
print('The area of the polygon is:',int(x))