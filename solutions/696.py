# Count Binary Substrings
class Solution:
    def runLengthEncoding(self, s):
        index = 0
        length = len(s)
        result = []
        while index < length:
            current = s[index]

            count = 1
            index += 1
            while index < length and current == s[index]:
                count += 1
                index += 1
            result.append((current, count))

        return result

    def countBinarySubstrings(self, s):
        encoding = self.runLengthEncoding(s)

        ans = 0

        index = 0
        length = len(encoding)

        while index < length - 1:
            current, next = encoding[index], encoding[index + 1]

            # the second element contains the consecutive number of `whatever the first element is`
            ans += min(current[1], next[1])

            index += 1

        return ans

if __name__ == "__main__":
    sol = Solution()
    s = "10101"
    print(sol.countBinarySubstrings(s))
