from typing import List, Tuple

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        def score(index, row) -> Tuple[int, int]:
            return (sum(row), index)

        scores = [score(index, row) for index, row in enumerate(mat)]
        scores.sort()
        return [idx for _, idx in scores[:k]]
