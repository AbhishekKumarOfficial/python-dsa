class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [-1 for i in range(k)]
        self.front = -1
        self.rear = -1
        self.size = k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.front += 1
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = value
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        if self.front == self.rear:
            self.front, self.rear = -1, -1
        else:
            self.front = (self.front + 1) % self.size
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.rear]

    def isEmpty(self) -> bool:
        return True if self.front == -1 else False

    def isFull(self) -> bool:
        return True if self.front is (self.rear + 1) % self.size else False

