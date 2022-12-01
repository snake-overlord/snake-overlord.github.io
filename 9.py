count = 0
f = open('9.txt')
for s in f:
    a = list(map(int, s.split()))
    t = sum(a) - sum(set(a))
    if len(a) - len(set(a)) == 1 and (sum(a) - 2*t)/4 <= t*2:
        count+=1
print(count)
