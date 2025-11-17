from typing import List


###
# 给你一个由若干 0 和 1 组成的数组 nums 以及整数 k。如果所有 1 都至少相隔 k 个元素，则返回 true ；否则，返回 false 。
#
# 简单题直接算
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        cnt = k
        for v in nums:
            if v == 1:
                if cnt < k:
                    return False
                cnt = 0
            else:
                cnt += 1
        return True
