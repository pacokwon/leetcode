# Count and Say

class Solution:
    def sayHelper(self, s):
        index = 0
        length = len(s)
        ans = ""
        while index < length:
            count = 1
            while index + 1 < length and s[index] == s[index + 1]:
                count += 1
                index += 1

            # once the loop is finished, it's either the end of the string or a different character
            # move to the next character
            num = s[index]
            index += 1
            ans += f"{count}{num}"

        return ans


    def countAndSay(self, n):
        base = "1"
        if n == 1:
            return base

        ans = base
        for _ in range(2, n + 1):
            ans = self.sayHelper(ans)

        return ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.countAndSay(10))
