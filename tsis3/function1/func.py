#1
def convert(gramm):
    return 28.3495231 * gramm

#2
def farentoc(F):
    return (5 / 9) * (F - 32)

#3
def solve(numheads,numlegs):
    rabbit = 0.5 * numlegs - numheads
    chickens = 2 * numheads - 0.5 * numlegs
    return (rabbit,chickens)

#4
def prime(n):
    if(n==1): return False
    if(n==2): return True
    if(n%2==0): return False

    x = int(n ** 0.5) + 1
    for i in range(3,x):
        if(n%i == 0): 
            return False
    return True
def filter_prime(numbers):
    filtered_list = []
    for i in numbers:
        if(prime(i)):
            filtered_list.append(i)
    return filtered_list

#5
def permute(a):
    n = len(a)
    i=0
    j=0
    for i in  range(n-2,-1,-1):
        if(a[i] < a[i+1]):
            break
    if(i < 0):
        a.reverse()
    else:
        for j in range(n-1,i,-1):
            if(a[j] > a[i]):
                break
        a[i], a[j] = a[j], a[i]
        st, end = i + 1, len(a)
        a[st:end] = a[st:end][::-1]
def prnt_prmttn(a):
    a = sorted(a)
    b = sorted(a, reverse = True)

    while a != b:
        print(''.join(a))
        permute(a)
    print(''.join(a))
a = [i for i in input()]
prnt_prmttn(a)

#6
def rvrs(s):
    s = s.split()
    s.reverse()
    return ' '.join(s)
s = input()   
print(rvrs(s))

#7
def has_33(num):
    for i in range(len(num)-1):
        if(num[i] == 3 and num[i+1] == 3):
            return True
    return False

#8
def spy_game(nums):
    for i in range(len(nums)-2):
        if nums[i] == 0 and nums[i+1] == 0 and nums[i+2] == 7:
            return True
    return False
s= input()
parts = s.split(' ')
numbs = [int(i) for i in parts]
print(spy_game(numbs))

#9
def volume(r):
    pi = 3.1415926535897931
    V = 4 / 3 * pi * r ** 3
    return V
n = int(input())
print(volume(n))

#10
def unique_list(n):
    unique = []
    for item in n :
        if item not in unique:
            unique.append(item)
    return unique

#11
def palindrome(s):
    if(s == s[::-1]):
        return True
    return False
word = input()
print(palindrome(word))

#12
def histogram(list):
    for n in list:
        output = ' '
        while(n>0):
            output += '*'
            n = n-1
        print(output)
histogram([4,9,7])

#13
import random

name = input("Hello! What is your name?\n")
print("Well, %s, I am thinking of a number between 1 and 20." % name)

secret = int(random.randint(1, 20))
input = int(input("Take a guess.\n"))
count = 1

while input != secret:
    if input < secret:
        print("Your guess is too low.")
    elif input > secret:
        print ("Your guess is too high.")
    input == int(input("Take a guess.\n"))
    count += 1

print ("Good job, %s! You guessed my number in %d guesses!" % (name, count))
