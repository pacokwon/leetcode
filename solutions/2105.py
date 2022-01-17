# Watering Plants II
class Solution:
    def minimumRefill(self, plants, capacityA, capacityB):
        # no tricks, a solution that does just what the problem asks us
        aliceIndex = 0
        bobIndex = len(plants) - 1

        aliceTank = capacityA
        bobTank = capacityB
        refillCount = 0

        while aliceIndex < bobIndex:
            alicePlant = plants[aliceIndex]
            if aliceTank < alicePlant:
                aliceTank = capacityA
                refillCount += 1
            aliceTank -= alicePlant

            bobPlant = plants[bobIndex]
            if bobTank < bobPlant:
                bobTank = capacityB
                refillCount += 1
            bobTank -= bobPlant

            aliceIndex += 1
            bobIndex -= 1

        if aliceIndex == bobIndex:
            plant = plants[aliceIndex]
            if aliceTank >= bobTank:
                if plant > aliceTank:
                    refillCount += 1
            else:
                if plant > bobTank:
                    refillCount += 1

        return refillCount

if __name__ == "__main__":
    sol = Solution()
    plants = [2,2,3,3]
    capacityA = 3
    capacityB = 3
    print(sol.minimumRefill(plants, capacityA, capacityB))
