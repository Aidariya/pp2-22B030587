def div(n):
    for i in range(n+1):
        if n%3==0 and n%4==0:
            yield i
n = int(input())
for num in div(n):
    print(num)