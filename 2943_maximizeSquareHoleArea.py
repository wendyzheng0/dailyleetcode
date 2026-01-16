from typing import List


###
# 给你两个整数 n 和 m，以及两个整数数组 hBars 和 vBars。网格由 n + 2 条水平线和 m + 2 条竖直线组成，形成 1x1 的单元格。网格中的线条从 1 开始编号。
# 你可以从 hBars 中 删除 一些水平线条，并从 vBars 中删除一些竖直线条。注意，其他线条是固定的，无法删除。
# 返回一个整数表示移除一些线条（可以不移除任何线条）后，网格中 正方形空洞的最大面积 。
#
# 当删除序号连续的一系列线条之后就可以得到比较大的一个空洞，所以分别计算横向和纵向的最长连续序列，然后取其中最小的个数就可以得到正方形空洞的最大面积。
class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        if len(hBars) == 0 or len(vBars) == 0:
            return 1

        def getContinueSeqLen(arr: List[int]):
            res = 0
            cnt = 1
            arr.sort()
            for i in range(1, len(arr)):
                if arr[i] == arr[i - 1] + 1:
                    cnt += 1
                else:
                    res = max(res, cnt)
                    cnt = 1
            return max(res, cnt)

        hlen = getContinueSeqLen(hBars)
        vlen = getContinueSeqLen(vBars)
        # print(f"hlen:{hlen}, vlen:{vlen}")
        return (min(hlen, vlen) + 1) ** 2
