class Solution:
    def reachNumber(self, target: int) -> int:
        numMoves = 1
        i = 0
        if target > 0:
            while True:
                i += numMoves
                if i == target:
                    break
                else:
                    numMoves = abs(numMoves) + 1
                    tepm = i + numMoves
                    if tepm > target:
                        numMoves = -numMoves
        else:
            while True:
                i -= numMoves
                if i == target:
                    break
                else:
                    numMoves = abs(numMoves) + 1
                    tepm = i - numMoves
                    if tepm < target:
                        numMoves = -numMoves

        return numMoves

f = Solution()
print(f.reachNumber(2))