def recur(int n):
    if n<=1:
        return 1
    return n*recur(n-1)

print(recur(5))