'''
假设有一个很长的花坛，一部分地块种植了花，另一部分却没有。可是，花不能种植在相邻的地块上，它们会争夺水源，两者都会死去。

给你一个整数数组 flowerbed 表示花坛，由若干 0 和 1 组成，其中 0 表示没种植花，1 表示种植了花。另有一个数 n ，能否在不打破种植规则的情况下种入 n 朵花？能则返回 true ，不能则返回 false 。
'''
flowerbed1 = [1, 0, 0, 0, 1]
n1 = 1
# 输出：true
flowerbed2 = [1, 0, 0, 0, 1]
n2 = 2
# 输出：false
flowerbed3 = [1, 0, 0, 0, 0, 1]
n3 = 2
# 输出：false
flowerbed4 = [0, 0, 1, 0, 1]
n4 = 1
# 输出：true
flowerbed5 = [0, 0, 1, 0, 0]
n5 = 2
# 输出：true
flowerbed6 = [1]
n6 = 0
# 输出：true


def canPlaceFlowers(flowerbed, n):
    m = 0
    if len(flowerbed) == 1:
        if n == 0:
            return True
        else:
            return (flowerbed[0] == 0)
    else:
        if flowerbed[0] == 0 and flowerbed[1] == 0:
            m += 1
            flowerbed[0] = 1
        if flowerbed[-1] == 0 and flowerbed[-2] == 0:
            m += 1
            flowerbed[-1] = 1
        if len(flowerbed) >= 3:
            for i in range(1, len(flowerbed)):
                if flowerbed[i] == flowerbed[i - 1] and flowerbed[i] == flowerbed[i + 1]:
                    flowerbed[i] = 1
                    m += 1
        return (m >= n)


canPlaceFlowers(flowerbed6, n6)


# 最优代码
# 亮点解析：给最前最后加一个[0]花盆
# class Solution:
#     def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
#         flowerbed = [0] + flowerbed + [0]
#         m = 0
#         for i in range(1, len(flowerbed)-1):
#             if flowerbed[i]==0 and flowerbed[i+1]==0 and flowerbed[i-1]==0:
#                 flowerbed[i] = 1
#                 m += 1
#         return (m >= n)
