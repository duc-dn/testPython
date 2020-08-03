arr = list(map(str, input().split()))
ten = [arr[i] for i in range(len(arr)) if i % 2 == 0]
dantoc = [arr[i] for i in range(len(arr)) if i % 2 == 1]
Dict = dict()
for i, j in zip(ten, dantoc):
    if j not in Dict: 
        Dict[j] = [i]
    else:
        Dict[j].append(i)
print(Dict[max(Dict, key = lambda i: len(Dict[i]))])