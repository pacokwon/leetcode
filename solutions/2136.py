# Earliest Possible Day of Full Bloom

from typing import List

class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        grow = list(enumerate(growTime))

        # sort by decreasing order of grow time
        # if grow time is equal, sort decreasing order of planting time
        grow.sort(key=lambda x: (-x[1], -plantTime[x[0]]))

        finishingTime = -1
        currentTime = 0
        for index, g in grow:
            # plant this thing
            currentTime += plantTime[index]

            # from currentTime, the plant will bloom at:
            bloomTime = currentTime + g
            finishingTime = max(bloomTime, finishingTime)

        return finishingTime

if __name__ == "__main__":
    sol = Solution()
    plantTime = [1,2,3,2]
    growTime = [2,1,2,1]
    plantTime = [1,4,3]
    growTime = [2,3,1]
    plantTime = [1]
    growTime = [1]
    print(sol.earliestFullBloom(plantTime, growTime))
