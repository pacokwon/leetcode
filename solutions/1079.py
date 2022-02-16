# Letter Tile Possibilities

from typing import List, Tuple

class Solution:
    def group(self, tiles: str) -> List[Tuple[str, int]]:
        length = len(tiles)
        index = 0

        grouped = []
        while index < length:
            val = tiles[index]
            count = 0
            while index < length and val == tiles[index]:
                count += 1
                index += 1
            grouped.append([val, count])

        return grouped

    def numTilePossibilities(self, t: str) -> int:
        tiles = ''.join(sorted(t))
        g = self.group(tiles)

        length = len(t)
        ans = 0
        def dfs(count, grouped):
            nonlocal ans
            if count == length:
                ans += 1
                return

            for el in grouped:
                if el[1] > 0:
                    el[1] -= 1
                    dfs(count + 1, grouped)
                    el[1] += 1

            dfs(length, grouped)

        dfs(0, g)

        # exclude the empty case
        return ans - 1

if __name__ == "__main__":
    sol = Solution()
    tiles = "AAABBC"
    print(sol.numTilePossibilities(tiles))
