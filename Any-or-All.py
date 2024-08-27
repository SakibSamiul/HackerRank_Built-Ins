n = int(input())
N = list(map(int, input().split()))
print((all(i > 0 for i in N)) and (any(str(p) == str(p)[::-1] for p in N)))
