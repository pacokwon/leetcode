# Rotate String

class Solution:
    def check(self, s: str, goal: str, start: int) -> bool:
        for i in range(len(s)):
            gi = (start + i) % len(s)
            if s[i] != goal[gi]:
                return False
        return True

    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        starts = [index for index, _ in enumerate(goal) if s[0] == goal[index]]
        if not starts:
            return False

        for start in starts:
            if self.check(s, goal, start):
                return True

        return False

if __name__ == "__main__":
    sol = Solution()
    s = "abcde"
    goal = "cdeab"
    s = "abcde"
    goal = "abced"
    s = "bbbacddceeb"
    goal = "ceebbbbacdd"
    print(sol.rotateString(s, goal))
