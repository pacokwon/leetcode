# ZigZag conversion

class Solution:
    def convert(self, s, numRows):
        """
        P     I     N
        A   L S   I G
        Y A   H R
        P     I
        In this example, we call P, I, N `pivots`.
        """
        if numRows == 1:
            return s

        length = len(s)

        # compute pivots
        # gap between the indices of two pivots is 2 * row - 2
        pivots = []
        index = 0
        while index < length:
            pivots.append(index)
            index += 2 * numRows - 2

        """
        A character might be left alone without a pivot that could reach it, such as:
        P     I
        A   L S
        Y A   H R
        P     I
        The R doesn't have a pivot that could reach it. So we just put in an additional pivot.
        """
        if index - numRows + 1 < length - 1:
            pivots.append(index)

        # first iteration
        chars = [s[index] for index in pivots if index < length]
        indices = []
        for index in pivots:
            if index - 1 >= 0:
                indices.append(index - 1)

            if index + 1 < length:
                indices.append(index + 1)

        # intermediate iterations
        for _ in range(numRows - 2):
            newIndices = []

            for (nth, index) in enumerate(indices):
                if index < length:
                    chars.append(s[index])

                if nth % 2 == 0:
                    if index + 1 < length:
                        newIndices.append(index + 1)
                else:
                    newIndices.append(index - 1)

            indices = newIndices

        # at the last iteration, ther will be duplicate indices
        for (nth, index) in enumerate(indices):
            if nth % 2 == 1: continue
            chars.append(s[index])

        return ''.join(chars)


if __name__ == "__main__":
    sol = Solution()
    s = "PAYPALISHIRING"
    numRows = {
    print(sol.convert(s, numRows))
