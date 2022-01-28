# All Paths From Source to Target

class Solution:
    def allPathsSourceTarget(self, graph):
        length = len(graph)

        SRC = 0
        DEST = length - 1

        visited = [False] * length
        # a path has max length
        path = [None] * length

        def dfs(v, visited, count, path, ans):
            visited[v] = True
            path[count] = v

            if v == DEST:
                ans.append(path[:count + 1])
                visited[v] = False
                return

            adj = graph[v]
            for u in adj:
                if not visited[u]:
                    dfs(u, visited, count + 1, path, ans)

            visited[v] = False

        ans = []
        dfs(SRC, visited, 0, path, ans)

        return ans

if __name__ == "__main__":
    sol = Solution()
    graph = [[1,2],[3],[3],[]]
    graph = [[4,3,1],[3,2,4],[3],[4],[]]
    print(sol.allPathsSourceTarget(graph))
