from typing import List
from math import inf


###
# 给你两个下标从 0 开始的字符串 source 和 target ，它们的长度均为 n 并且由 小写 英文字母组成。
# 另给你两个下标从 0 开始的字符数组 original 和 changed ，以及一个整数数组 cost ，其中 cost[i] 代表将字符 original[i] 更改为字符 changed[i] 的成本。
# 你从字符串 source 开始。在一次操作中，如果 存在 任意 下标 j 满足 cost[j] == z  、original[j] == x 以及 changed[j] == y 。你就可以选择字符串中的一个字符 x 并以 z 的成本将其更改为字符 y 。
# 返回将字符串 source 转换为字符串 target 所需的 最小 成本。如果不可能完成转换，则返回 -1 。
# 注意，可能存在下标 i 、j 使得 original[j] == original[i] 且 changed[j] == changed[i] 。
#
# 用Floyd算法解决。mindist[i][j] 表示将字符 i 转换为字符 j 的最小成本。每次只用前k+1个字符来更新mindist。
class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        orda = ord('a')
        mindist = [[inf] * 26 for _ in range(26)]
        for i in range(26):
            mindist[i][i] = 0
        for orig, ch, c in zip(original, changed, cost):
            ordorig, ordch = ord(orig) - orda, ord(ch) - orda
            mindist[ordorig][ordch] = min(mindist[ordorig][ordch], c)

        for k in range(26):
            for i in range(26):
                if mindist[i][k] == inf:
                    continue
                for j in range(26):
                    mindist[i][j] = min(mindist[i][j], mindist[i][k] + mindist[k][j])

        # print(mindist)
        res = 0
        for s, t in zip(source, target):
            if s == t:
                continue
            ords, ordt = ord(s) - orda, ord(t) - orda
            res += mindist[ords][ordt]
        return res if res < inf else -1
