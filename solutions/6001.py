class Solution:
    def maximize(self, num: int) -> int:
        strnum = sorted(str(num), reverse=True)
        return int(''.join(strnum))

    def minimize(self, num: int) -> int:
        strnum = sorted(str(num))
        length = len(strnum)


        if strnum[0] == '0':
            index = 0
            while index < length and strnum[index] == '0':
                index += 1

            if index == length:
                return 0

            strnum[0], strnum[index] = strnum[index], strnum[0]

        return int(''.join(strnum))

    def smallestNumber(self, num: int) -> int:
        if num < 0:
            return -self.maximize(-num)
        else:
            return self.minimize(num)

if __name__ == "__main__":
    sol = Solution()
    n = 310
    n = -7605
    print( sol.smallestNumber(n) )
