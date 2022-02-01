# Keep Multiplying Found Values by Two

class Solution:
    def findFinalValue(self, nums, original):
        while True:
            found = False
            for n in nums:
                if n == original:
                    found = True
                    original *= 2
                    break

            if not found:
                return original

