from typing import List
from collections import Counter


###
# 在一条无限长的公路上有 n 辆汽车正在行驶。汽车按从左到右的顺序按从 0 到 n - 1 编号，每辆车都在一个 独特的 位置。
# 给你一个下标从 0 开始的字符串 directions ，长度为 n 。directions[i] 可以是 'L'、'R' 或 'S' 分别表示第 i 辆车是向 左 、向 右 或者 停留 在当前位置。每辆车移动时 速度相同 。
# 碰撞次数可以按下述方式计算：
# 当两辆移动方向 相反 的车相撞时，碰撞次数加 2 。
# 当一辆移动的车和一辆静止的车相撞时，碰撞次数加 1 。
# 碰撞发生后，涉及的车辆将无法继续移动并停留在碰撞位置。除此之外，汽车不能改变它们的状态或移动方向。
# 返回在这条道路上发生的 碰撞总次数 。
#
# 左边的'L'和右边的'R'都不会碰撞，先删掉这两部分。剩下部分里每个'L'和'R'都会碰撞一次，而'S'不会碰撞。
class Solution:
    def countCollisions(self, directions: str) -> int:
        s = directions.lstrip('L').rstrip('R')
        return len(s) - s.count('S')

    def countCollisions1(self, directions: str) -> int:
        n = len(directions)
        lr = directions.find('R')
        ls = directions.find('S')
        left = min(lr if lr >= 0 else n, ls if ls >= 0 else n)
        right = max(directions.rfind('L'), directions.rfind('S'))
        if left >= right:
            return 0
        cnt = Counter(directions[left:right + 1])
        return cnt['R'] + cnt['L']


if __name__ == "__main__":
    s = Solution()
    # 测试用例
    print(s.countCollisions("RLRSLL"))  # 应该返回5: R-L(+2), R-S(+1), R-L(+2) = 5
    print(s.countCollisions("LLRR"))    # 应该返回4: L-R(+2), L-R(+2) = 4
    print(s.countCollisions("SSRSSRLLRSLLRSRSSRLRRRRRRRSSRLLRRRLRRRSSSSR"))  # 复杂测试

