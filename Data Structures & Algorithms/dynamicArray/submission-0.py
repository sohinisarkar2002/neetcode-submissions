class DynamicArray:
    
    def __init__(self, capacity: int):
        self.size = 0
        self.cap = capacity
        self.ar = [None] * capacity

    def get(self, i: int) -> int:
        return self.ar[i]

    def set(self, i: int, n: int) -> None:
        self.ar[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.cap:
            self.resize()

        self.ar[self.size] = n
        self.size += 1

    def popback(self) -> int:
        self.size -= 1
        return self.ar[self.size]

    def resize(self) -> None:
        self.cap *= 2
        new_ar = [None] * self.cap

        for i in range(self.size):
            new_ar[i] = self.ar[i]

        self.ar = new_ar

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.cap
