# Rings and Rods

from collections import defaultdict

class Solution:
    def countPoints(self, rings: str) -> int:
        length = len(rings)
        acc = defaultdict(int)
        # r -> 1, g -> 2 -> b -> 4
        for i in range(length // 2):
            color = rings[i * 2]
            bit = 1 if color == 'R' else 2 if color == 'G' else 4

            pos = ord(rings[i * 2 + 1]) - ord('0')
            acc[pos] = acc[pos] | bit

        return len([None for _, val in acc.items() if val == 7])

if __name__ == "__main__":
    sol = Solution()
    rings = "B0B6G0R6R0R6G9"
    rings = "B0R0G0R9R0B0G0"
    rings = "G4"
    print( sol.countPoints(rings) )
