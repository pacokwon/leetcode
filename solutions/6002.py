class Bitset:
    def __init__(self, size):
        self.bitmap = 0
        self.size = size
        self.cnt = 0

    def fix(self, idx):
        if self.bitmap & (1 << idx) == 0:
            self.bitmap = self.bitmap | (1 << idx)
            self.cnt += 1

    def unfix(self, idx):
        if self.bitmap & (1 << idx):
            self.bitmap = self.bitmap ^ (1 << idx)
            self.cnt -= 1

    def flip(self):
        self.bitmap = self.bitmap ^ ((1 << self.size) - 1)
        self.cnt = self.size - self.cnt

    def all(self):
        return self.cnt == self.size

    def one(self):
        return self.bitmap > 0

    def count(self):
        return self.cnt

    def toString(self):
        a = bin(self.bitmap)[2:]
        return a[::-1] + '0' * (self.size - len(a))
