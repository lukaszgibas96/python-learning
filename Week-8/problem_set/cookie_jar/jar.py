class Jar:
    def __init__(self, capacity=12):
        self._capacity = capacity
        if self._capacity <= 0:
            raise ValueError
        self.cookies = 0

        

    def __str__(self):
        return self.cookies * "🍪"

    def deposit(self, n):
        if n < 0:
            raise ValueError
        if self.cookies + n > self.capacity:
            raise ValueError
        
        self.cookies = self.cookies + n

    def withdraw(self, n):
        if n < 0:
            raise ValueError
        if self.cookies - n < 0:
            raise ValueError
        self.cookies = self.cookies - n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self.cookies