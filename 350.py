from collections import Counter
from typing import List
#快速排序
# m = [5,2,3,9,7,8,12]
# m.sort()
# print(m)
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        length1, length2 = len(nums1), len(nums2)
        intersection = list()
        index1 = index2 = 0
        while index1 < length1 and index2 < length2:
            if nums1[index1] < nums2[index2]:
                index1 += 1
            elif nums1[index1] > nums2[index2]:
                index2 += 1
            else:
                intersection.append(nums1[index1])
                index1 += 1
                index2 += 1

        return intersection

s = Solution()
num1=[1,2,2,3,5,6,5]
num2=[2,2,3,5,6,8,9]
print(s.intersect(num1,num2))
