###
# 设计一个敲击计数器，使它可以统计在过去 5 分钟内被敲击次数。（即过去 300 秒）
# 您的系统应该接受一个时间戳参数 timestamp (单位为 秒 )，并且您可以假定对系统的调用是按时间顺序进行的(即 timestamp 是单调递增的)。几次撞击可能同时发生。
# 实现 HitCounter 类:
# HitCounter() 初始化命中计数器系统。
# void hit(int timestamp) 记录在 timestamp ( 单位为秒 )发生的一次命中。在同一个 timestamp 中可能会出现几个点击。
# int getHits(int timestamp) 返回 timestamp 在过去 5 分钟内(即过去 300 秒)的命中次数。
#
# 由于hit和getHits传入的timestamp都是单调递增的，所以可以用一个queue来保存接受hit的时间戳。
class HitCounter:

    def __init__(self):
        self.data = deque()

    def hit(self, timestamp: int) -> None:
        self.data.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        while self.data and self.data[0] < timestamp - 299:
            self.data.popleft()
        return len(self.data)

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)