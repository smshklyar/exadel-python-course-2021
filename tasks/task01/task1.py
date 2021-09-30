import math
for i in range(1, 1000):
    b = []
    mem = i
    for x in [100, 10, 1]:
        b.append(i // x)
        i %= x
    t = 0
    lensq = int(math.log10(mem))+1
    t = sum([z**lensq for z in b])
    if mem == t:
        print(t)