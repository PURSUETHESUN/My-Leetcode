class Solution:
    def minimumLength(self, s: str) -> int:
        n = len(s)
        i, j = 0, n - 1
        while i < j:
            if s[i] != s[j]:
                break
            else:
                while i < j:
                    if s[i] == s[i + 1]:
                        i += 1
                    else:
                        break

                while i < j:
                    if s[j] == s[j - 1]:
                        j -= 1
                    else:
                        break
                i += 1
                j -= 1
        if i == j:
            return 1
        elif i > j:
            return 0
        else:
            return j - i + 1

S = Solution()
print(S.minimumLength("cabaabac"))