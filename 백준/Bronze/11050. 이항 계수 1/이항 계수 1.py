n, k = map(int, input().split())

def fact(n):
    if n == 0 or n == 1:
        return 1
    else :
        return n * fact(n-1)

print( fact(n) // (fact(n-k)*fact(k)))