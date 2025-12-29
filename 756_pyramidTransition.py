from typing import List
from functools import cache
from collections import defaultdict


###
# 你正在把积木堆成金字塔。每个块都有一个颜色，用一个字母表示。每一行的块比它下面的行 少一个块 ，并且居中。
# 为了使金字塔美观，只有特定的 三角形图案 是允许的。一个三角形的图案由 两个块 和叠在上面的 单个块 组成。模式是以三个字母字符串的列表形式 allowed 给出的，其中模式的前两个字符分别表示左右底部块，第三个字符表示顶部块。
# 例如，"ABC" 表示一个三角形图案，其中一个 “C” 块堆叠在一个 'A' 块(左)和一个 'B' 块(右)之上。请注意，这与 "BAC" 不同，"B" 在左下角，"A" 在右下角。
# 你从作为单个字符串给出的底部的一排积木 bottom 开始，必须 将其作为金字塔的底部。
# 在给定 bottom 和 allowed 的情况下，如果你能一直构建到金字塔顶部，使金字塔中的 每个三角形图案 都是在 allowed 中的，则返回 true ，否则返回 false 。
#
# pyramidTransition1是从小到大建造金字塔，bottom的编号是0，一直到n-1。依次建造底为bottom[:i]的金字塔，直到底为bottom。这个方法不好剪枝，比较耗时。
# pyramidTransition2是从底到顶一层层建造金字塔。每完成一层就记录这层的记录。当没有建成失败回溯的时候，这些出现过的记录就是曾经不成功的记录，从而可以跳过。这个方法比上一个稍快
# pyramidTransition的方法是从底到顶一层层建造金字塔，每次把下一层的一个字符换成上一层的一个字符，直到下一层只剩两个字符时，把这两个字符所有可能转换为的值和上一层组合，再继续建造上上层。
class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        valid = defaultdict(list)
        for s in allowed:
            valid[s[:2]].append(s[2])

        @cache
        def fill(lower, upper):
            if len(upper) > 2 and not fill(upper, ''):
                return False
            if len(lower) == 2:
                if len(upper) == 0:
                    return len(valid[lower]) > 0
                else:
                    return any(fill(upper + v, '') for v in valid[lower])
            else:
                return any(fill(lower[1:], upper + v) for v in valid[lower[:2]])
        return fill(bottom, '')

    def pyramidTransition2(self, bottom: str, allowed: List[str]) -> bool:
        valid = defaultdict(list)
        for s in allowed:
            valid[s[:2]].append(s[2])

        n = len(bottom)
        f = [[] for _ in range(n)]
        f[-1] = bottom
        vis = set()

        def dfs(i, j):
            if i < 0:
                return True
            prefix = ''.join(f[i])
            if j == i + 1:
                vis.add(prefix)
                return dfs(i - 1, 0)
            if prefix in vis:
                # print(f"{prefix} is tried but failed, skip")
                return False
            s = f[i + 1][j] + f[i + 1][j + 1]
            for cand in valid[s]:
                f[i].append(cand)
                # print(f"try {i}: {''.join(f[i])}")
                if dfs(i, j + 1):
                    return True
                f[i].pop()
            return False
        return dfs(n - 2, 0)

    def pyramidTransition1(self, bottom: str, allowed: List[str]) -> bool:
        valid = dict()
        for pair in allowed:
            if pair[:2] not in valid:
                valid[pair[:2]] = []
            valid[pair[:2]].append(pair[2])
        n = len(bottom)
        f = [[None] * (i + 1) for i in range(n - 1, -1, -1)]
        f[0] = [v for v in bottom]
        # print(f)

        def dfs(idx, i):
            if idx >= n:
                return True
            s = ''.join(f[i - 1][idx - i:idx - i + 2])
            if s in valid:
                if i >= idx:
                    newi = 1
                    newidx = idx + 1
                else:
                    newi = i + 1
                    newidx = idx
                # print(f"try idx:{idx}, i:{i}, val:{valid[s]}, newidx:{newidx}, newi:{newi}")
                for cand in valid[s]:
                    f[i][idx - i] = cand
                    if dfs(newidx, newi):
                        return True
            return False
        return dfs(1, 1)



if __name__ == "__main__":
    s = Solution()
    print(s.pyramidTransition("BCD", ["BCC","CDE","CEA","FFF"])) # true
    print(s.pyramidTransition("AAAA", ["AAB","AAC","BCD","BBE","DEF"])) # false
    print(s.pyramidTransition("ABCD", ["ABC","BCA","CDA","ABD","BCE","CDF","DEA","EFF","AFF"])) # true
    print(s.pyramidTransition("DB", ["BDD","ACA","CBA","BDC","AAC","DCB","ABC","DDA","CCB"])) # false
