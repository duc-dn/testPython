a, b, c = list(map(int, input().split())), list(map(int, input().split())), list(map(int, input().split()))
x = []
y = []
for i in a, b, c:
    x.append(i[0]), y.append(i[1])
for i in x:
    if x.count(i) == 1:
        print(i,end=' ')
for i in y:
    if y.count(i) == 1:
        print(i,end=' ') 

