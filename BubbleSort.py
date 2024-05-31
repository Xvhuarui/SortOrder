# 冒泡排序
import random

ini = []
i = 0
while i < 10:
    ini.append(random.randint(-1000, 1000))
    i += 1
print(ini)

k = 9
while k > 0:
    j = 0
    while j < k:
        if ini[j] > ini[j+1]:
            center = ini[j+1]
            ini[j+1] = ini[j]
            ini[j] = center
            j += 1
        else:
            j += 1
    k -= 1
print(ini)
