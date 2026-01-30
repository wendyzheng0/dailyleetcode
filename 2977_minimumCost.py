from typing import List
from math import inf


###
# 给你两个下标从 0 开始的字符串 source 和 target ，它们的长度均为 n 并且由 小写 英文字母组成。
# 另给你两个下标从 0 开始的字符串数组 original 和 changed ，以及一个整数数组 cost ，其中 cost[i] 代表将字符串 original[i] 更改为字符串 changed[i] 的成本。
# 你从字符串 source 开始。在一次操作中，如果 存在 任意 下标 j 满足 cost[j] == z  、original[j] == x 以及 changed[j] == y ，你就可以选择字符串中的 子串 x 并以 z 的成本将其更改为 y 。 你可以执行 任意数量 的操作，但是任两次操作必须满足 以下两个 条件 之一 ：
# 在两次操作中选择的子串分别是 source[a..b] 和 source[c..d] ，满足 b < c  或 d < a 。换句话说，两次操作中选择的下标 不相交 。
# 在两次操作中选择的子串分别是 source[a..b] 和 source[c..d] ，满足 a == c 且 b == d 。换句话说，两次操作中选择的下标 相同 。
# 返回将字符串 source 转换为字符串 target 所需的 最小 成本。如果不可能完成转换，则返回 -1 。
# 注意，可能存在下标 i 、j 使得 original[j] == original[i] 且 changed[j] == changed[i] 。
#
# 先对可以转换的字符串做编码，然后用Floyd算法计算任意编码之间转换的最小成本。
# 然后建立一个后缀树便于查找任意字串可以转换的目标及成本。
# 用动态规划计算最小成本。dp[i] 表示将source[:i]转换为target[:i]的最小成本。当source[i] == target[i]时，dp[i] = dp[i-1]。
# 否则，遍历所有可以转换的子串，找到最小成本。  
class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        chardict = dict()
        id2char = []
        idx = 0
        for s in original:
            if s not in chardict:
                chardict[s] = idx
                id2char.append(s)
                idx += 1
        for s in changed:
            if s not in chardict:
                chardict[s] = idx
                id2char.append(s)
                idx += 1
        mincost = [[inf] * idx for _ in range(idx)]
        for i in range(idx):
            mincost[i][i] = 0
        for s, t, c in zip(original, changed, cost):
            sid, tid = chardict[s], chardict[t]
            mincost[sid][tid] = min(mincost[sid][tid], c)

        for k in range(idx):
            for i in range(idx):
                if mincost[i][k] == inf:
                    continue
                for j in range(idx):
                    mincost[i][j] = min(mincost[i][j], mincost[i][k] + mincost[k][j])
        # print(chardict)
        # print(mincost)

        trie = {'value': None, 'children': {}}
        for s, code in chardict.items():
            node = trie
            for c in s[::-1]:
                if c not in node['children']:
                    node['children'][c] = {'value': c, 'children': {}}
                node = node['children'][c]
            srcid = chardict[s]
            node['target'] = dict()
            for tid, tcost in enumerate(mincost[srcid]):
                if tcost < inf:
                    node['target'][tid] = tcost
        # print(trie)

        dp = [0] + [inf] * len(source)
        for i in range(len(source)):
            if source[i] == target[i]:
                dp[i + 1] = dp[i]
            node = trie
            for j in range(i, -1, -1):
                if source[j] not in node['children']:
                    break
                else:
                    node = node['children'][source[j]]
                if 'target' in node and target[j:i + 1] in chardict:
                    exp = chardict[target[j:i + 1]]
                    if exp in node['target']:
                        dp[i + 1] = min(dp[i + 1], dp[j] + node['target'][exp])
                        # print(f"convert {source[j:i + 1]} to {target[j:i + 1]}, dp[{i + 1}] is {dp[i + 1]}, {dp[j]}")
        return dp[-1] if dp[-1] < inf else -1
