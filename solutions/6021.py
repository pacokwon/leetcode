class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        """
        Approach:
        let [front,back] = pattern

        let i_b be the index of first occurrence of back, in text.
        let i_f be the index of last occurrence of front, in text.

        Insert front before i_b, and back before i_f.
        We know how much of pattern that produces. Choose the larger one.
        """

        front = pattern[0]
        back = pattern[1]

        if front == back:
            cnt = text.count(front)
            return cnt * (cnt - 1) // 2 + cnt

        frontIndices = []
        backIndices = []

        for index, c in enumerate(text):
            if c == front:
                frontIndices.append(index)
            elif c == back:
                backIndices.append(index)

        ans = max(len(frontIndices), len(backIndices))
        index = 0
        cnt = 0
        for bi in backIndices:
            while index < len(frontIndices) and frontIndices[index] < bi:
                index += 1
                cnt += 1
            ans += cnt
        return ans
