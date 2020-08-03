a = list(map(int, input().split()))
count = 0
for i in range(len(a)): 
    for j in range(i):
        if a[i] <= a[j] and a[j] > a[j + 1]:
            count += 1
    print(count, end=' ')
    count = 0
    
