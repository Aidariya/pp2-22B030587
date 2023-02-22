a = int(input())
def square(N):
    for i in range(N):
        yield i**2

for sq in square(a):
    print(sq)