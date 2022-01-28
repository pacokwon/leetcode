# Search a 2D Matrix

class Solution:
    def searchRow(self, matrix, target):
        left, right = 0, len(matrix) - 1
        while left < right:
            mid = (left + right) // 2
            mv = matrix[mid][0]
            # print(f'left: {left}, mid: {mid}, right: {right}, mv: {mv}')

            if target < mv:
                right = mid - 1
            else:
                left = mid

                if left + 1 == right:
                    if matrix[right][0] <= target:
                        return right
                    else:
                        return left

        return left

    def searchMatrix(self, matrix, target):
        rowIndex = self.searchRow(matrix, target)
        row = matrix[rowIndex]
        left, right = 0, len(row) - 1
        while left <= right:
            mid = (left + right) // 2
            if target == row[mid]:
                return True
            elif target > row[mid]:
                left = mid + 1
            else:
                right = mid - 1

        return False

if __name__ == "__main__":
    sol = Solution()
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 12
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 3
    print(sol.searchMatrix(matrix, target))
