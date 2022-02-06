# Find Good Days to Rob the Bank

from typing import List

class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        length = len(security)

        # we start at the index `time`
        # we keep track of whether or not the previous and next `time` elements are decreasing

        # dp for decreasing
        ddp = [0] * length
        ddp[0] = 0
        for index in range(1, length):
            if security[index - 1] >= security[index]:
                ddp[index] = ddp[index - 1] + 1
            else:
                ddp[index] = 0

        idp = [0] * length
        idp[-1] = 0
        for index in range(length - 2, -1, -1):
            if security[index] <= security[index + 1]:
                idp[index] = idp[index + 1] + 1
            else:
                idp[index] = 0

        return [index for index, _ in enumerate(security) if ddp[index] >= time and idp[index] >= time]

if __name__ == "__main__":
    sol = Solution()
    security = [4,3,2,1]
    time = 1
    print( sol.goodDaysToRobBank(security, time) )
