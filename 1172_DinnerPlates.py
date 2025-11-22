from sortedcontainers import SortedList


###
# 我们把无限数量 ∞ 的栈排成一行，按从左到右的次序从 0 开始编号。每个栈的的最大容量 capacity 都相同。
# 实现一个叫「餐盘」的类 DinnerPlates：
# DinnerPlates(int capacity) - 给出栈的最大容量 capacity。
# void push(int val) - 将给出的正整数 val 推入 从左往右第一个 没有满的栈。
# int pop() - 返回 从右往左第一个 非空栈顶部的值，并将其从栈中删除；如果所有的栈都是空的，请返回 -1。
# int popAtStack(int index) - 返回编号 index 的栈顶部的值，并将其从栈中删除；如果编号 index 的栈是空的，请返回 -1。
#
# 这题偷懒了，用了sortedlist，用heap也可以。如果保持stacks最右边永远是非空的stack可以省掉self.notempty变量。
class DinnerPlates:

    def __init__(self, capacity: int):
        self.stacks = []
        self.avail = SortedList()
        self.notempty = SortedList()
        self.capacity = capacity

    def push(self, val: int) -> None:
        # self.showinfo("push")
        if len(self.avail) == 0:
            idx = len(self.stacks)
            self.stacks.append([val])
            if len(self.stacks[idx]) < self.capacity:
                self.avail.add(idx)
            self.notempty.add(idx)
        else:
            idx = self.avail[0]
            self.stacks[idx].append(val)
            if len(self.stacks[idx]) == self.capacity:
                del self.avail[0]
            if len(self.stacks[idx]) == 1:
                self.notempty.add(idx)

    def pop(self) -> int:
        # self.showinfo("pop")
        if len(self.notempty) == 0:
            return -1
        idx = self.notempty[-1]
        val = self.stacks[idx][-1]
        del self.stacks[idx][-1]
        if len(self.stacks[idx]) == 0:
            del self.notempty[-1]
        if len(self.stacks[idx]) == self.capacity - 1:
            self.avail.add(idx)
        return val

    def showinfo(self, tag):
        print(tag)
        print(self.stacks)
        print(self.avail)
        print(self.notempty)

    def popAtStack(self, index: int) -> int:
        # self.showinfo(f"popAtStack[{index}]")
        if 0 <= index < len(self.stacks) and len(self.stacks[index]) > 0:
            val = self.stacks[index][-1]
            del self.stacks[index][-1]
            if len(self.stacks[index]) == self.capacity - 1:
                self.avail.add(index)
            if len(self.stacks[index]) == 0:
                self.notempty.remove(index)
            return val
        else:
            return -1

# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)