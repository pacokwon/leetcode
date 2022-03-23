class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        count = 0
        while target != startValue:
            if target < startValue:
                return startValue - target + count

            if target % 2 == 0:
                target = target // 2
            else:
                target += 1

            count += 1

        return count
