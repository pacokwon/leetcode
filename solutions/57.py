# Insert Interval

class Solution:
    def insert(self, intervals, newInterval):
        ans = []
        [nst, nen] = newInterval
        for index, [st, en] in enumerate(intervals):
            if en < nst:
                ans.append(intervals[index])
            elif nen < st:
                # can return now
                ans.append([nst, nen])
                return ans + intervals[index:]
            else:
                nst = min(nst, st)
                nen = max(nen, en)

        ans.append([nst, nen])
        return ans

if __name__ == "__main__":
    sol = Solution()
    intervals = [[1,3],[6,9]]
    newInterval = [2,5]

    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    newInterval = [4,18]
    print(sol.insert(intervals, newInterval))
