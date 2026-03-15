# nums1 = [1, 2, 3, 0, 0, 0]
# m = 3
# nums2 = [2, 5, 6]
# n = 3
# nums3 = [0] * m
# for i in range(m):
#     nums3[i] = nums1[i]
# nums3 = nums3 + nums2
# nums3.sort()
# nums1 = nums3
# print(nums1)
leaders_1 = ['Elon Mask', 'Tim Cook']
leaders_2 = ['Yang Zhou', 'Bill Gates']

leaders_4 = ['Elon Mask', 'Tim Cook']
leaders_1[:] = leaders_2[:]
print(leaders_1)