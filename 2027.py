class Solution:
    def minimumMoves(self, s: str) -> int:
        n = len(s)
        res = 0
        i = 0
        while i < n:
            if s[i] == 'X':
                res += 1
                i += 3
            else:
                i += 1
        return res
S = Solution()
print(S.minimumMoves("0X0X"))