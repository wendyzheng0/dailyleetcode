###
# 现在有一个尺寸为 width * height 的矩阵 M，矩阵中的每个单元格的值不是 0 就是 1。
# 而且矩阵 M 中每个大小为 sideLength * sideLength 的 正方形 子阵中，1 的数量不得超过 maxOnes。
# 请你设计一个算法，计算矩阵中最多可以有多少个 1。
#
# 题目难度更多是在于怎么确定应该如何摆放这些1.根据官方题解：只需要遍历第一个正方形，也就是最左上角的正方形，然后对于其中的每一个格子，计算出「如果将该格子填充 1，那么在整个矩形中可以填充多少个格子，使得它们互相没有影响（即互相不在同一个正方形内）」的数量。最后选择互相不影响的数量最多的 maxOnes 个格子进行填充即可。
# 链接：https://leetcode.cn/problems/maximum-number-of-ones/solutions/2477555/ju-zhen-zhong-1-de-zui-da-shu-liang-by-l-12g3/
# 按照解题思路实现。认识了divmod函数，可以同时计算商和余数，不用计算两次除法了。
class Solution:
    def maximumNumberOfOnes(self, width: int, height: int, sideLength: int, maxOnes: int) -> int:
        maxPos = []
        widthnum, widthremainder = divmod(width, sideLength)
        heightnum, heightremainder = divmod(height, sideLength)
        for i in range(sideLength):
            for j in range(sideLength):
                w = widthnum + (1 if widthremainder > i else 0)
                h = heightnum + (1 if heightremainder > j else 0)
                maxPos.append(w * h)
        maxPos.sort(reverse=True)
        # print(maxPos)
        return sum(maxPos[:maxOnes])