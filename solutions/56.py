# Merge Intervals

class Solution:
    def merge(self, intervals):
        intervals = sorted(intervals, key=lambda x: x[0])
        acc = intervals[0]
        ans = []
        for itv in intervals:
            if acc[1] >= itv[0]:
                acc[1] = max(acc[1], itv[1])
            else:
                ans.append(acc)
                acc = itv
        ans.append(acc)

        return ans

if __name__ == "__main__":
    sol = Solution()
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    intervals = [[1,4],[4,5]]
    intervals = [[1,4]]
    intervals = [[1,4],[2,3]]
    print(sol.merge(intervals))
