import copy
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def fun(x: int,l1: List):
            if len(l1) == k:
                d_copy = copy.deepcopy(l1)#用到深拷贝，原因是回溯出去后我需要修改l1的值，这里为了防止已加入result的列表值发生修改
                result.append(d_copy)
                return
            else:
                for j in range(x+1, n + 1):
                    l1.append(j)
                    fun(j, l1)
                    l1.pop()
        for i in range(1, n + 1):
            path = [i]
            fun(i, path)
        return result
f = Solution()
print(f.combine(4,2))