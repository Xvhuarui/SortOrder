# 插入排序
import random

ini = []
i = 0
while i < 10:
    ini.append(random.randint(-1000, 1000))
    i += 1
print(ini)

j = 1
while j < 10:
    k = j
    while k > 0:
        if ini[k] < ini[k-1]:
            center = ini[k - 1]
            ini[k - 1] = ini[k]
            ini[k] = center
            k -= 1
        else:
            k -= 1
    j += 1
print(ini)

