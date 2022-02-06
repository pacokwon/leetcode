import bisect

class SORTracker:

    def __init__(self):
        self.arr = []
        self.i = 0

    def add(self, name: str, score: int) -> None:
        bisect.insort(self.arr, (-score, name))

    def get(self) -> str:
        val = self.arr[self.i][1]
        self.i += 1
        return val
