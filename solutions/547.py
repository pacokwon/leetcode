# Number Of Provinces

class Solution:
    def findCircleNum(self, isConnected):
        checked = [False] * len(isConnected)

        def dfs(start, checked):
            checked[start] = True

            dests = isConnected[start]
            for dest, reachable in enumerate(dests):
                if reachable == 1 and not checked[dest]:
                    dfs(dest, checked)

        ans = 0
        index = 0
        while index < len(checked):
            val = checked[index]

            if not val:
                # check
                dfs(index, checked)
                ans += 1

            index += 1

        return ans

if __name__ == "__main__":
    sol = Solution()
    isConnected = [[1,1,0],[1,1,0],[0,0,1]]
    isConnected = [[1,0,0],[0,1,0],[0,0,1]]
    print(sol.findCircleNum(isConnected))
