import math
for i in range(1, 1000):
    b = []
    mem = i
    while i > 0:
        b.insert(0, i % 10)
        i = i // 10
    lensq = int(math.log10(mem))+1
    t = sum([z**lensq for z in b])
    if mem == t:
        print(t)
