###
# 给你一个字符串 s ，请你去除字符串中重复的字母，使得每个字母只出现一次。需保证 返回结果的字典序最小（要求不能打乱其他字符的相对位置）。
#
# 遍历字符串记录各个字符最后出现的位置。然后边遍历边构造结果，如果当前字符已经在结果里就跳过，否则和结果的前一个字符比较，如果前
# 一个字符比当前字符大而且后面还有出现，那就替换掉。
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        lastpos = {c: i for i, c in enumerate(s)}
        res = []
        removeset = set()
        for idx, c in enumerate(s):
            if c in removeset:
                continue
            while res and res[-1] >= c and lastpos[res[-1]] > idx:
                removeset.remove(res.pop())
            res.append(c)
            removeset.add(c)

        return ''.join(res)


if __name__ == "__main__":
    solution = Solution()
    print(solution.removeDuplicateLetters("abacb")) #abc
    print(solution.removeDuplicateLetters("bcabc")) #abc
    print(solution.removeDuplicateLetters("cbacdcedbc")) #acdeb
    print(solution.removeDuplicateLetters("cbacdcbdac")) #adbc