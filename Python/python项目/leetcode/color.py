nums = [2, 0, 2, 1, 1, 0]
j = 0
k = 0
for i in range(len(nums)):
    if nums[i] == 0:
        j += 1
    elif nums[i] == 1:
        k += 1
nums2 = [2] * len(nums)
for i in range(0, j):
    nums2[i] = 0
for i in range(j, j + k):
    nums2[i] = 1
print(nums2)
