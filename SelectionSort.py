# 选择排序 O(n**2)
import random

ini = []
i = 0
while i < 10:
    ini.append(random.randint(-1000, 1000))
    i += 1
print(ini)

j = 0
k = 0
l = 10
fi = []
while k < 10:
    j = 0
    center = ini[j]
    while j < l:
        if center > ini[j]:
            center = ini[j]
        j += 1
    ini.remove(center)
    fi.append(center)
    k += 1
    l -= 1
print(fi)
