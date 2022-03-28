from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        for i in range(len(s) - 1, -1, -1):
            c = s[i]
            if c in last:
                continue
            last[c] = i

        ans = []

        index = 0
        count = 0
        while index < len(s):
            c = s[index]
            count += 1

            if index == last[c]:
                ans.append(count)
                count = 0
                index += 1
                continue

            l = last[c]
            index += 1
            while index < l:
                d = s[index]
                count += 1
                if last[d] > l:
                    l = last[d]
                index += 1
            ans.append(count + 1)
            count = 0
            index += 1

        return ans

