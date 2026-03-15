nums = [1, 3, 5, 6]
target = 5
l = 0
r = len(nums) - 1
m = (l + r) // 2
while l <= r:
    if target > nums[m]:
        l = m + 1
        m = (l + r) // 2
    elif target < nums[m]:
        r = m - 1
        m = (l + r) // 2
    else:
        print(m)
        break
print(m)