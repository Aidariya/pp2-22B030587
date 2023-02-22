import math
def area(h,a1,a2):
    return 0.5 *h*(a1+a2)

h = int(input())
a1 = int(input())
a2 = int(input())
s = area(h,a1,a2)

print("Height : ", h)
print("Base, first value: " , a1)
print("Base, second value: " , a2)
print("Expected Output: " , s)