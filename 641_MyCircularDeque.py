###
# 设计实现双端队列。
# 实现 MyCircularDeque 类:
# MyCircularDeque(int k) ：构造函数,双端队列最大为 k 。
# boolean insertFront()：将一个元素添加到双端队列头部。 如果操作成功返回 true ，否则返回 false 。
# boolean insertLast() ：将一个元素添加到双端队列尾部。如果操作成功返回 true ，否则返回 false 。
# boolean deleteFront() ：从双端队列头部删除一个元素。 如果操作成功返回 true ，否则返回 false 。
# boolean deleteLast() ：从双端队列尾部删除一个元素。如果操作成功返回 true ，否则返回 false 。
# int getFront() )：从双端队列头部获得一个元素。如果双端队列为空，返回 -1 。
# int getRear() ：获得双端队列的最后一个元素。 如果双端队列为空，返回 -1 。
# boolean isEmpty() ：若双端队列为空，则返回 true ，否则返回 false  。
# boolean isFull() ：若双端队列满了，则返回 true ，否则返回 false 。
#
# 对于python来说，直接头尾插入和删除头和尾会更快。
class MyCircularDeque:

    def __init__(self, k: int):
        self.val = [0] * (k + 1)
        self.head = self.tail = 0
        self.k = k

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.val[self.head - 1] = value
        self.head = (self.head - 1) % (self.k + 1)
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.val[self.tail] = value
        self.tail = (self.tail + 1) % (self.k + 1)
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.head = (self.head + 1) % (self.k + 1)
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.tail = (self.tail - 1) % (self.k + 1)
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.val[self.head]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.val[self.tail - 1]

    def isEmpty(self) -> bool:
        return self.head == self.tail

    def isFull(self) -> bool:
        return (self.tail - self.head) % (self.k + 1) == self.k


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()