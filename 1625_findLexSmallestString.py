from math import gcd, inf


###
# 给你一个字符串 s 以及两个整数 a 和 b 。其中，字符串 s 的长度为偶数，且仅由数字 0 到 9 组成。
# 你可以在 s 上按任意顺序多次执行下面两个操作之一：
# 累加：将  a 加到 s 中所有下标为奇数的元素上（下标从 0 开始）。数字一旦超过 9 就会变成 0，如此循环往复。例如，s = "3456" 且 a = 5，则执行此操作后 s 变成 "3951"。
# 轮转：将 s 向右轮转 b 位。例如，s = "3456" 且 b = 1，则执行此操作后 s 变成 "6345"。
# 请你返回在 s 上执行上述操作任意次后可以得到的 字典序最小 的字符串。
# 如果两个字符串长度相同，那么字符串 a 字典序比字符串 b 小可以这样定义：在 a 和 b 出现不同的第一个位置上，字符串 a 中的字符出现在字母表中的时间早于 b 中的对应字符。例如，"0158” 字典序比 "0190" 小，因为不同的第一个位置是在第三个字符，显然 '5' 出现在 '9' 之前。
class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        n = len(s)
        sint = [int(v) for v in s]
        ag = gcd(a, 10)
        bg = gcd(b, n)

        # 计算使得lowidx位最小时的数组值
        def addax(nums, lowidx):
            # 计算nums[lowidx]所能取的最小值是对gcd(a, 10)取模的值
            # 由于所有数字都会增加同样的数值，所以用diff加到其他位上
            target = nums[lowidx] % ag
            diff = target - nums[lowidx]
            if diff != 0:
                for i in range(lowidx, n, 2):
                    nums[i] = (nums[i] + diff) % 10

        i = start = 0
        res = [inf]
        # 列举每个可能在0位的数字移动到0位时，可以取的最小值。
        # 由于只有奇数位可以用累加的方法改变数值，如果这些可能
        # 被移动到0位的数字没法移动到奇数位上（gcd(b,n)是偶数），
        # 就没法改变数值，只需要计算它移到0位时奇数位所能取到的
        # 最小值就可以了。而如果gcd(b,n)是奇数，我们就可以先移动到
        # 奇数位，用累加方法取最小值，然后再移动到0位上。
        while True:
            news = sint[i:] + sint[:i]   # 右移i位
            print(i)
            print(news)
            # use addition method to make it small
            addax(news, 1)
            if bg % 2 == 1:
                addax(news, 0)
            print(news)
            res = min(res, news)
            i = (i + b) % n
            if i == start:
                break
        return ''.join(map(str, res))
