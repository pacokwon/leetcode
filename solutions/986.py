# Interval List Intersections

class Solution:
    def intervalIntersection(self, firstList, secondList):
        fl, sl = len(firstList), len(secondList)
        fi, si = 0, 0

        inter = []
        while fi < fl and si < sl:
            f, s = firstList[fi], secondList[si]

            if s[0] <= f[1] <= s[1]:
                inter.append([max(s[0], f[0]), f[1]])
                fi += 1
            elif f[0] <= s[1] <= f[1]:
                inter.append([max(s[0], f[0]), s[1]])
                si += 1
            else:
                if f[1] > s[1]:
                    si += 1
                else:
                    fi += 1

        return inter

if __name__ == "__main__":
    sol = Solution()
    firstList = [[0,2],[5,10],[13,23],[24,25]]
    secondList = [[1,5],[8,12],[15,24],[25,26]]

    firstList = [[1,3],[5,9]]
    secondList = []
    print(sol.intervalIntersection(firstList, secondList))
