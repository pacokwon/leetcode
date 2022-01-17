# Roman to Integer

class Solution:
    def romanToInt(self, s):
        conversionTable = {
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900
        }

        mappings = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        index = 0
        length = len(s)
        result = 0
        while index < length:
            pair = s[index:index + 2]
            if pair in conversionTable:
                result += conversionTable[pair]
                index += 2
            else:
                result += mappings[s[index]]
                index += 1

        return result

if __name__ == "__main__":
    sol = Solution()
    inp = "MCMXCIV"
    print(sol.romanToInt(inp))
