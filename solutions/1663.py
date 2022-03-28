class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        def toChar(n):
            return chr(97 + n - 1)

        ans = [''] * n
        i = 0
        while i < n:
            # how many spaces left to fill?
            left = n - i
            if k < left:
                # you got `left` spaces to fill,
                # but k is not enough
                # won't happen with a valid input
                pass
            if k - 26 < (left - 1):
                # if you subtract 26 from k,
                # there won't be enough k to
                # fill the remaining spaces.
                # subtract just enough so that
                # the remaining spaces can be filled
                # with just a's
                # k - x = left - 1
                ans[i] = toChar(k - (left - 1))
                i += 1
                while i < n:
                    ans[i] = 'a'
                    i += 1
                break

            ans[i] = 'z'
            k -= 26
            i += 1

        return ''.join(ans)[::-1]
