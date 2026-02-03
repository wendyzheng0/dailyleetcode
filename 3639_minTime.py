###
# 给你一个长度为 n 的字符串 s 和一个整数数组 order，其中 order 是范围 [0, n - 1] 内数字的一个 排列。
# 从时间 t = 0 开始，在每个时间点，将字符串 s 中下标为 order[t] 的字符替换为 '*'。
# 如果 子字符串 包含 至少 一个 '*' ，则认为该子字符串有效。
# 如果字符串中 有效子字符串 的总数大于或等于 k，则称该字符串为 活跃 字符串。
# 返回字符串 s 变为 活跃 状态的最小时间 t。如果无法变为活跃状态，返回 -1。
#
# 字符串长度为n时可以有n*(n+1)//2个子字符串，每增加一个*计算剩下的字母可以组成的不活跃字符串个数，直到不活跃的小于total-k个
class Solution:
    def minTime(self, s: str, order: List[int], k: int) -> int:
        # total substr: n + (n-1) + (n-2) +...+ 1 = (n+1)*n/2
        # change one char to *, substr contains *: n
        n = len(s)
        arr = [[0, n - 1]]
        total = n * (n + 1) // 2
        if k > total:
            return -1
        elif k == total:
            return n - 1
        target = total - k
        for t, idx in enumerate(order):
            p = bisect_left(arr, [idx, idx])
            if p == len(arr) or arr[p][0] > idx:
                p -= 1
            precnt = arr[p][1] - arr[p][0] + 1
            total -= precnt * (precnt + 1) // 2
            if arr[p][0] == idx:
                if arr[p][1] == idx:
                    del arr[p]
                else:
                    arr[p][0] = idx + 1
                    curcnt = precnt - 1
                    total += curcnt * (curcnt + 1) // 2
            elif arr[p][1] == idx:
                arr[p][1] = idx - 1
                curcnt = precnt - 1
                total += curcnt * (curcnt + 1) // 2
            else:
                end = arr[p][1]
                arr[p][1] = idx - 1
                arr.insert(p + 1, [idx + 1, end])
                curcnt1 = arr[p][1] - arr[p][0] + 1
                curcnt2 = end - idx
                total += curcnt1 * (curcnt1 + 1) // 2
                total += curcnt2 * (curcnt2 + 1) // 2
            # print(f"{t}: {idx}, {total}")
            if total <= target:
                return t
        return -1
