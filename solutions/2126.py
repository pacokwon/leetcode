# Destroying Asteroids

from typing import List

class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        for ast in asteroids:
            if mass >= ast:
                mass += ast
            else:
                return False
        return True
