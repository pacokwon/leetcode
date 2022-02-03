# Minimum Moves to Reach Target Score

class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        ans = 0
        while target > 1:
            if maxDoubles > 0:
                if target % 2 != 0:
                    target -= 1
                else:
                    target //= 2
                    maxDoubles -= 1
            else:
                ans += target - 1
                break

            ans += 1

        return ans

if __name__ == "__main__":
    sol = Solution()
    target = 5
    maxDoubles = 1
    target = 19
    maxDoubles = 2
    target = 10
    maxDoubles = 4
    target = 100
    maxDoubles = 1
    print( sol.minMoves(target, maxDoubles) )
