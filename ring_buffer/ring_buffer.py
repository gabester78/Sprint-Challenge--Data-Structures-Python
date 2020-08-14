from collections import deque


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.index = 0
        self.queue = deque()

    def append(self, item):
        if len(self.queue) == self.capacity:
            self.queue[self.index] = item
        else:
            self.queue.append(item)
        self.index = (self.index + 1) % self.capacity

    def get(self):
        the_one_ring = []
        for i in self.queue:
            the_one_ring.append(i)
        return the_one_ring
