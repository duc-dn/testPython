a = int(input())
b = input()
c = {}
ok = True
for i in b:
    if i in c:
        c[i] += 1
    else:
        c[i] = 1
c = c.items()
d = [i[1] for i in c]
e = [i[0] for i in c]
for i in range(len(d) - 1):
    if d[i] != d[i+1] :
        print('-1')
        ok = False
        break
x = ''
if a!= d[1]:
    print('-1')
elif ok == True and a == d[1]:
    for i in e:
        x += i
    print(x * a,end='')



