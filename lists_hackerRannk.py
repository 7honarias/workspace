N = int(input())
    
    
l = []
i = 0
while i < N:
    temp = input().split()
    
    if temp[0] == 'print':
        print(l)
    if temp[0] == 'insert':
        l.insert(int(temp[1]), int(temp[2]))
    if temp[0] == 'append':
        l.append(int(temp[1]))
    if temp[0] == 'pop':
        l.pop()
    if temp[0] == 'sort':
        l.sort()
    if temp[0] == 'reverse':
        l.reverse()
    if temp[0] == 'remove':
        l.remove(int(temp[1]))
        
    i += 1