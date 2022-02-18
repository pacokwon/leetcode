# Remove K Digits

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)

        if n == k:
            return "0"
        if n == k + 1:
            return min(num)

        stack = []
        for n in num:
            if not stack or k == 0:
                stack.append(n)
            else:
                while stack and n < stack[-1] and k > 0:
                    k -= 1
                    stack.pop()
                stack.append(n)

        while k > 0:
            stack.pop()
            k -= 1

        index = 0
        while index < len(stack) and stack[index] == '0':
            index += 1

        if index == len(stack):
            return '0'
        else:
            return ''.join(stack[index:])

if __name__ == "__main__":
    sol = Solution()
    num = "10"
    k = 1
    num = "112"
    k = 1
    print(sol.removeKdigits(num, k))
