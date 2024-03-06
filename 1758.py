class Solution:
    def minOperations(self, s: str) -> int:
        num1 = 0
        num2 = 1
        l1 = list(s)
        l2 = list(s)
        n = len(s)
        i = j = 0
        while i < n - 1:
            if l1[i] == l1[i+1]:
                num1 += 1
                if l1[i+1] == '0':
                    l1[i+1] = '1'
                else:
                    l1[i+1] = '0'
            i += 1
        if l2[0] == '0':
            l2[0] = '1'
            while j < n - 1:
                if l2[j] == l2[j+1]:
                    num2 += 1
                    if l2[j+1] == '0':
                        l2[j+1] = '1'
                    else:
                        l2[j+1] = '0'
                j += 1
        else:
            l2[0] = '0'
            while j < n - 1:
                if l2[j] == l2[j+1]:
                    num2 += 1
                    if l2[j+1] == '0':
                        l2[j+1] = '1'
                    else:
                        l2[j+1] = '0'
                j += 1
        return min(num1,num2)

S = Solution()
print(S.minOperations("10010100"))