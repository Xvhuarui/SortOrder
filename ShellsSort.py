# 希尔排序 O(n*logn)到O(n**2)
import random

ini = []
i = 0
while i < 10:
    ini.append(random.randint(-1000, 1000))
    i += 1
print(ini)

ran = 10 / 2  # 范围大小
l = 0  # 列表下标每次前进数
while ran >= 1:
    while l < 10 - ran + 1:
        j = 1  # 列表下标第几位
        while j < ran:
            k = j  # 两两对比插入
            while k > 0:
                if ini[k + l] < ini[k + l - 1]:
                    center = ini[k + l - 1]
                    ini[k + l - 1] = ini[k + l]
                    ini[k + l] = center
                    k -= 1
                else:
                    k -= 1
            j += 1
        l += 1
        print(ini)
    ran //= 2
print(ini)
