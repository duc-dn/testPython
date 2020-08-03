a = set(map(str, input().split()))
b = set(map(str, input().split()))
print('2 mon: ', a & b)
print('1 mon: ', a ^ b)