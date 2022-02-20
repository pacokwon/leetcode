# Count Operations to Obtain Zero

class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        ops = 0

        while not (num1 == 0 or num2 == 0):
            if num1 > num2:
                ops += num1 // num2
                num1 = num1 % num2
            else:
                ops += num2 // num1
                num2 = num2 % num1

        return ops

if __name__ == "__main__":
    sol = Solution()
    num1 = 1
    num2 = 1
    print(sol.countOperations(num1, num2))
