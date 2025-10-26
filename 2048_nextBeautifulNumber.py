from collections import Counter
import time
from typing import List
from collections import defaultdict


###
# 如果整数  x 满足：对于每个数位 d ，这个数位 恰好 在 x 中出现 d 次。那么整数 x 就是一个 数值平衡数 。
# 给你一个整数 n ，请你返回 严格大于 n 的 最小数值平衡数 。
#
# 暴力法（nextBeautifulNumber2），因为总有一个数可以满足条件，所以从n开始，每次加1，检查是否是数值平衡数。如果数值比较大容易超时
# 动态规划法（nextBeautifulNumber），先找到target里面必须替换的idx，然后从idx往前遍历，尝试用更大的数字去替换。每次替换完计算
# 剩余的位置时候能容纳必须出现的数字，如果还有空位，则寻找没用到的数字里是否有可能填补这些空位的组合，如果没有，替换失败，尝试下一个。
# 如果所有替换都失败，则尝试下一个idx。
class Solution:
    def nextBeautifulNumber2(self, n: int) -> int:
        while True:
            n += 1
            cnt = Counter(str(n))
            if all(int(v) == c for v, c in cnt.items()):
                return n

    def getSeq(self, valid, pos):
        if pos == 0:
            return []
        validlen = len(valid)
        # f[i][j]: if we can select x numbers from valid[:i] whoes sum is j, it's True.
        # f[i][j] = f[i - 1]][j - valid[i]] if j > valid[i] or f[i - 1][j]
        f = [[False] * (pos + 1) for _ in range(validlen + 1)]
        f[0][0] = True
        for i in range(validlen):
            for j in range(pos + 1):
                f[i + 1][j] = f[i][j]
                if j >= valid[i]:
                    f[i + 1][j] = f[i + 1][j] or f[i][j - valid[i]]
            # print(f"{i + 1}: {f[i + 1]}")
        if f[validlen][pos] == 0:
            return None
        j = pos
        ans = []
        while j > 0:
            for i in range(validlen):
                if f[i + 1][j] and j >= valid[i] and f[i][j - valid[i]]:
                    ans = [valid[i]] * valid[i] + ans
                    j -= valid[i]
                    break
        return ans

    def nextBeautifulNumber(self, n: int) -> int:
        target = [0] + [int(v) for v in list(str(n))]
        cnt = defaultdict(int)
        for idx in range(1, len(target)):
            v = target[idx]
            if v != 0 and cnt[v] < v:
                cnt[v] += 1
            else:
                break
        else:
            cnt[v] -= 1
        # try to replace target[idx] with a larger digit and check whether
        # there is valid number
        while idx >= 0:
            # try from target[idx] + 1, no need to seperate whether the digit
            # is in original target or not, that will be too complicated.
            for rep in range(target[idx] + 1, 10):
                if cnt[rep] >= rep:
                    continue
                # print(f"try use {rep} to replace target[{idx}]")
                cnt[rep] += 1
                res = target[:idx]
                res.append(rep)

                free = len(target) - len(res)
                # tofill is the numbers must be filled in the remaining positions
                tofill = []
                for vv, c in cnt.items():
                    if c != 0 and vv != 0:
                        tofill.extend([vv] * (vv - c))
                # print(f"has {free} positions, need to fill: {tofill}")
                if len(tofill) > free:
                    cnt[rep] -= 1
                    continue
                else:
                    # after filling the must digits, find available digits to fill
                    # remaining positions
                    subtarget = free - len(tofill)
                    if subtarget > 0:
                        valid = [i for i in range(1, 10) if cnt[i] == 0]
                        left = self.getSeq(valid, subtarget)
                        if left is None:
                            # print(f"no combine can get {subtarget}")
                            cnt[rep] -= 1
                            continue
                        tofill.extend(left)
                    # find one combination
                    tofill.sort()
                    res.extend(tofill)
                    ret = ''.join([str(v) for v in res])
                    return int(ret)
            idx -= 1
            if idx > 0:
                cnt[target[idx]] -= 1

        return ''


if __name__ == '__main__':
    sol = Solution()
    print(sol.nextBeautifulNumber(1))
    print(sol.nextBeautifulNumber(1000))
    print(sol.nextBeautifulNumber(3000))
    print(sol.nextBeautifulNumber(1822))
    start = time.time()
    print(sol.nextBeautifulNumber(123456789))
    end = time.time()
    print(f"time: {end - start}")
    start = time.time()
    print(sol.nextBeautifulNumber2(123456789))
    end = time.time()
    print(f"time: {end - start}")