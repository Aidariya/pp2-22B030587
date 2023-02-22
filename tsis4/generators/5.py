n = int(input())
def retrn(n):
    while n>=0:
        yield n
        n-=1
for i in retrn(n):
    print(i)