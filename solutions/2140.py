# Solving Questions With Brainpower

from typing import List

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        # first thoughts: dp?
        length = len(questions)
        dp = [[0, 0] for _ in range(length)]

        index = length - 1
        while index >= 0:
            [points, brainpower] = questions[index]

            nextSolvable = index + 1 + brainpower

            # 0 is when you decided to SOLVE this question
            dp[index][0] = points + (max(dp[nextSolvable]) if nextSolvable < length else 0)

            # 1 is when you decided to SKIP this question
            dp[index][1] = max(dp[index + 1]) if index + 1 < length else 0

            index -= 1

        return max(dp[0])

if __name__ == "__main__":
    sol = Solution()
    questions = [[3,2],[4,3],[4,4],[2,5]]
    questions = [[1,1],[2,2],[3,3],[4,4],[5,5]]
    print( sol.mostPoints(questions) )
