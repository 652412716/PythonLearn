class my_queue:

    def __init__(self, k: int):
        self.k = k
        self.front_num = 0
        self.rear_num = 0
        self.is_front = False

        self.queue = [None for i in range(k)]

    def enQueue(self, value: int) -> bool:
        if self.rear_num <= self.k - 1:
            if self.queue[self.rear_num] is None:
                self.queue[self.rear_num] = value
                self.rear_num += 1

                if self.rear_num == self.k:
                    self.rear_num = 0
                return True
            else:
                return False

    def deQueue(self) -> bool:
        if self.front_num <= self.k - 1:
            if self.queue[self.front_num] is not None:
                self.is_front = True
                self.queue[self.front_num] = None
                self.front_num += 1
                if self.front_num == self.k:
                    self.front_num = 0

                return True
            else:
                return False

    def Front(self) -> int:
        front_num = self.front_num
        if self.queue[front_num] is not None:
            return self.queue[front_num]
        else:
            return -1

    def Rear(self) -> int:
        rear_num = self.rear_num - 1
        if rear_num < 0:
            rear_num = self.k - 1
        if self.queue[rear_num] is not None:
            return self.queue[rear_num]
        else:
            return -1

    def isEmpty(self) -> bool:
        none_num = self.queue.count(None)
        if none_num == self.k:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if None in self.queue:
            return False
        else:
            return True

    def print_queue(self):
        print(self.queue)


new_queue = my_queue(2)
print(new_queue.enQueue(4))
print(new_queue.Rear())
print(new_queue.enQueue(9))
print(new_queue.deQueue())
new_queue.print_queue()
print(new_queue.Front())