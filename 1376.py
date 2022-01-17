# Time Needed to Inform All Employees

class Solution:
    def employees(self, n, manager):
        employee = [[] for _ in range(n)]
        for index, m in enumerate(manager):
            if m == -1: continue
            employee[m].append(index)
        return employee

    def aux(self, headID, employee, informTime):
        if not employee[headID]:
            return 0

        ans = 0
        for e in employee[headID]:
            ans = max(ans, self.aux(e, employee, informTime))

        return ans + informTime[headID]

    def numOfMinutes(self, n, headID, manager, informTime):
        employee = self.employees(n, manager)
        return self.aux(headID, employee, informTime)

if __name__ == "__main__":
    sol = Solution()
    n = 7
    headID = 2
    manager = [2,2,-1,2,2,2, 0]
    informTime = [3,0,1,0,0,0, 0]
    print(sol.numOfMinutes(n, headID, manager, informTime))
