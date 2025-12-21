from typing import List


###
# 给定由 n 个字符串组成的数组 strs，其中每个字符串长度相等。
# 选取一个删除索引序列，对于 strs 中的每个字符串，删除对应每个索引处的字符。
# 比如，有 strs = ["abcdef", "uvwxyz"]，删除索引序列 {0, 2, 3}，删除后 strs 为["bef", "vyz"]。
# 假设，我们选择了一组删除索引 answer，那么在执行删除操作之后，最终得到的数组的元素是按 字典序（strs[0] <= strs[1] <= strs[2] ... <= strs[n - 1]）排列的，然后请你返回 answer.length 的最小可能值。
#
# 贪心。从左到右遍历每一列，从上到下遍历每一个字符串。如果当前列的字符比前一行的字符串小，则删除当前列。
# 如果当前行的字符和前一行的字符串相同，则记录相等的字符的起止行，加入到下一次需要审查的区间。
# 如果当前列的字符比前一行的字符串大，则继续遍历。
# 如果遍历完了这一列不需要删除，则更新需要审查的区间，否则不更新。
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        zone = [[0, n]]
        res = 0
        idx = 0
        while zone and idx < len(strs[0]):
            # print(zone)
            nextzone = []
            for start, end in zone:
                p1 = start
                p2 = None
                for row in range(start + 1, end):
                    if strs[row][idx] < strs[row - 1][idx]:
                        # print(f"{row} is invalid, remove {idx}")
                        res += 1
                        break
                    elif strs[row][idx] == strs[row - 1][idx]:
                        p2 = row
                    else:
                        if p2 is not None:
                            nextzone.append([p1, row])
                            p2 = None
                        p1 = row
                else:
                    if p2 is not None:
                        nextzone.append([p1, end])
                    continue
                break
            else:
                zone = nextzone
            idx += 1
        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.minDeletionSize(["ca","bb","ac"])) # 1
    print(solution.minDeletionSize(["xc","yb","za"])) # 0
    print(solution.minDeletionSize(["zyx","wvu","tsr"])) # 3
    print(solution.minDeletionSize(["cab","bab","abc","dba","dba"])) # 2
    print(solution.minDeletionSize(["xga","xfb","yfa"])) # 1
    print(solution.minDeletionSize(["vkpphftpeutkfbrlbmqmahunjgeaol","fprnxczfmzcethrhhnujagbkcqjopp","yivlvyuxtnpwpsgpjejmmcykjkggnw","gjegryvechocvjsrnfykeywfcwenlx","ntfvoekvlpmoorosprmozdduzzxmsk","lsksvvpxxoludxxltlakelxxnfieiu","cegqlvawbdwzazpqtlusqhbfymytxz","kandmcbmxijbtasuvaraecglrhxsgg","yhjzmmfkwqfwavnrvokzckhugsdzbm","ivgpveqosuslpamnyaifdnbliwndhv"])) # 16