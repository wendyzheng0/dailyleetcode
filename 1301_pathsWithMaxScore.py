from typing import List

###
# 给你一个正方形字符数组 board ，你从数组最右下方的字符 'S' 出发。
# 你的目标是到达数组最左上角的字符 'E' ，数组剩余的部分为数字字符 1, 2, ..., 9 或者障碍 'X'。在每一步移动中，你可以向上、向左或者左上方移动，可以移动的前提是到达的格子没有障碍。
# 一条路径的 「得分」 定义为：路径上所有数字的和。
# 请你返回一个列表，包含两个整数：第一个整数是 「得分」 的最大值，第二个整数是得到最大得分的方案数，请把结果对 10^9 + 7 取余。
# 如果没有任何路径可以到达终点，请返回 [0, 0] 。
#
# 由于每个点的路径值只受到右边，下边和右下三个点的影响，可以用动态规划的思想从右往左从下往上遍历，记录路径最大值以及路径数量。实际反过来从终点向起点遍历也是一样的。
class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        n = len(board)
        preline = [[0, 0] for _ in range(n)]
        curline = [[0, 0] for _ in range(n)]
        preline[-1][1] = 1
        for j in range(n - 2, -1, -1):
            if board[-1][j] == 'X' or preline[j + 1][1] == 0:
                preline[j] = [0, 0]
            else:
                preline[j] = [int(board[-1][j]) + preline[j + 1][0], 1]
        # print(preline)
        for i in range(n - 2, -1, -1):
            if board[i][-1] == 'X' or preline[-1][1] == 0:
                curline[-1] = [0, 0]
            else:
                curline[-1] = [int(board[i][-1]) + preline[-1][0], 1]
            for j in range(n - 2, -1, -1):
                if board[i][j] == 'X':
                    curline[j] = [0, 0]
                else:
                    cand = [preline[j + 1], preline[j], curline[j + 1]]
                    cand.sort(reverse=True)
                    maxvalue = cand[0][:]
                    if cand[1][0] == maxvalue[0]:
                        maxvalue[1] += cand[1][1]
                    if cand[2][0] == maxvalue[0]:
                        maxvalue[1] += cand[2][1]
                    if board[i][j] != 'E' and maxvalue[1] != 0:
                        maxvalue[0] += int(board[i][j])
                    curline[j] = maxvalue
            preline, curline = curline, preline
            # print(preline)
        preline[0][1] = preline[0][1] % 1_000_000_007
        return preline[0]
