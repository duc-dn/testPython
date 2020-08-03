a = {'hung': 'kinh', 'duc': 'kinh', 'manh': 'muong', 'dinh': 'hoa', 'linh': 'hoa'}
b = a.items()
b = [i[1] for i in b]
c = [b.count(i) for i in b]
d = {}
for i in b:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
for i in d:
    if d[i] == max(c):
        for j in a:
            if i == a[j]:
                print(j)


    