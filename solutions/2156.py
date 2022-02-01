# Find Substring With Given Hash Value

class Solution:
    def subStrHash(self, s, power, modulo, k, hashValue):
        slen = len(s)

        def toInt(index):
            return ord(s[index]) - 96

        def computeHash(index):
            hash = 0
            for i in range(k - 1, -1, -1):
                hash = hash * power + ord(s[index + i]) - 96
            return hash % modulo

        ans = -1
        last = slen - k
        hash = computeHash(last)
        pk = pow(power, k, modulo)
        if hash == hashValue:
            ans = last

        for i in range(last - 1, -1, -1):
            hash = (hash * power + toInt(i)) % modulo
            hash = (hash - toInt(i + k) * pk) % modulo
            if hash == hashValue:
                ans = i

        return s[ans:ans+k]
