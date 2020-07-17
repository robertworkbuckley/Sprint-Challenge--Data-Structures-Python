class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None] * capacity

    def append(self, item):
        # if self.current == 0
        oldest = self.current + 1
        if oldest == self.capacity:
            oldest = 0

        self.storage[self.current] = item
        self.current = oldest

    def get(self):
        return [item for item in self.storage if item]

