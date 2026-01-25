from typing import List


###
# 你被给定一个 m × n 的二维网格 rooms ，网格中有以下三种可能的初始化值：
# -1 表示墙或是障碍物
# 0 表示一扇门
# INF 无限表示一个空的房间。然后，我们用 231 - 1 = 2147483647 代表 INF。你可以认为通往门的距离总是小于 2147483647 的。
# 你要给每个空房间位上填上该房间到 最近门的距离 ，如果无法到达门，则填 INF 即可。
#
# 开始的时候用广度优先搜索一层一层找记录步数并更新距离，但很奇怪的是竟然速度慢很多。最后改成直接在扩展节点的时候就更新距离，并且
# 直接更新而不是跟步数比较，竟然快了很多。
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        m, n = len(rooms), len(rooms[0])
        q = [(i, j) for i in range(m) for j in range(n) if rooms[i][j] == 0]
        DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        while q:
            cx, cy = q.pop(0)
            for dx, dy in DIRS:
                xx, yy = cx + dx, cy + dy
                if 0 <= xx < m and 0 <= yy < n and rooms[xx][yy] == 2147483647:
                    rooms[xx][yy] = rooms[cx][cy] + 1
                    q.append((xx, yy))
