#1
import math
l = list(map(int, input().split()))
print(math.prod(l)) 

#2
s = input()
lower = [
    1 if str(i).islower() else 0
    for i in s
]
upper = [
    1 if str(i).isupper() else 0
    for i in s
]
print('lowercase count: ',sum(lower))
print('uppercase count: ',sum(upper))

#3
s = str(input())
rvr_s = ''.join(reversed(s))
if rvr_s == s:
    print("Palindrome")
else:
    print("Not Palindrome")

#4
from time import sleep
from math import sqrt
n = int(input())
t = int(input())
sleep(t/1000)
print(f'Square root of {n} after {t} miliseconds is {sqrt(n)}'.format(n,t))

#5
n = tuple(map(int, input().split()))
print(all(n))