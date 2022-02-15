# Rotate Image

from typing import List

class Solution:
    def helper(self, mat: List[List[int]], offset: int) -> None:
        n = len(mat)
        low = offset
        high = n - 1 - offset

        def getFour(off):
            return [(low, low + off), (low + off, high), (high, high - off), (high - off, low)]

        def read(tup):
            return mat[tup[0]][tup[1]]

        def write(m, val, to):
            m[to[0]][to[1]] = val

        for o in range(high - low):
            [c1, c2, c3, c4] = getFour(o)
            v1 = read(c1)
            v2 = read(c2)
            v3 = read(c3)
            v4 = read(c4)
            write(mat, v1, c2)
            write(mat, v2, c3)
            write(mat, v3, c4)
            write(mat, v4, c1)


    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        offset = n // 2
        for off in range(offset):
            self.helper(matrix, off)

if __name__ == "__main__":
    from pprint import pprint
    sol = Solution()
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    sol.rotate(matrix)
    pprint(matrix)
