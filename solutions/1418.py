from typing import List
from collections import defaultdict

class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        table = defaultdict(lambda: defaultdict(int))
        foods = set()

        for [_, tableNo, food] in orders:
            table[tableNo][food] += 1
            foods.add(food)

        ans = [None] * (len(table) + 1)
        header = ["Table", *sorted(foods)]
        ans[0] = header

        for rowIndex, tn in enumerate(sorted(table.keys(), key=lambda x: int(x)), 1):
            row = [""] * len(header)
            row[0] = tn
            tbl = table[tn]

            for index, food in enumerate(header):
                if index == 0: continue
                row[index] = str(tbl[food])
            ans[rowIndex] = row

        return ans
