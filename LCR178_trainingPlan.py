from typing import List
from collections import Counter


###
# 教学过程中，教练示范一次，学员跟做三次。该过程被混乱剪辑后，记录于数组 actions，其中 actions[i] 表示做出该动作的人员编号。请返回教练的编号。
#
# 纯粹计数。
class Solution:
    def trainingPlan(self, actions: List[int]) -> int:
        cnt = Counter(actions)
        for k, v in cnt.items():
            if v == 1:
                return k
        return -1
