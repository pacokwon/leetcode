# Remove Covered Internals

from typing import List

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        ans = 0
        index = 0
        while index < len(intervals):
            [s, e] = intervals[index]
            ans += 1
            index += 1
            while index < len(intervals) and s <= intervals[index][0] and intervals[index][1] <= e:
                index += 1
        return ans

if __name__ == "__main__":
    sol = Solution()
    intervals = [[1,4],[3,6],[2,8]]
    intervals = [[1,4],[2,3],[3,10]]
    intervals = [[1,2],[1,4],[3,4]]
    print(sol.removeCoveredIntervals(intervals))
