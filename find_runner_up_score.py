n = int(input())
arr = map(int, input().split())
    
l = list(arr)
l.sort()
m = max(l)
while max(l) == m:
    l.remove(m)
print(max(l))