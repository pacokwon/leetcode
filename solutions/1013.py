class Solution:
    def canThreePartsEqualSum(self, arr):
        totalSum = sum(arr)
        if totalSum % 3 != 0:
            return False

        third = totalSum // 3

        # i need a synonym for sum, so i don't resort to korean
        hap = 0
        count = 0
        index = 0
        while index < len(arr):
            num = arr[index]

            hap += num
            if hap == third:
                hap = 0
                count += 1

                if count == 3:
                    index += 1
                    break

            index += 1

        if count < 3:
            return False

        hap = 0
        while index < len(arr):
            hap += arr[index]
            index += 1

        return hap == 0

if __name__ == "__main__":
    sol = Solution()
    inp = [0,0,0,0]
    # inp = [0,2,1,-6,6,-7,9,1,2,0,1]
    print(sol.canThreePartsEqualSum(inp))
