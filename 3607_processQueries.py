from heapq import heappop, heappush
from typing import List


###
# 给你一个整数 c，表示 c 个电站，每个电站有一个唯一标识符 id，从 1 到 c 编号。
# 这些电站通过 n 条 双向 电缆互相连接，表示为一个二维数组 connections，其中每个元素 connections[i] = [ui, vi] 表示电站 ui 和电站 vi 之间的连接。直接或间接连接的电站组成了一个 电网 。
# 最初，所有 电站均处于在线（正常运行）状态。
# 另给你一个二维数组 queries，其中每个查询属于以下 两种类型之一 ：
# [1, x]：请求对电站 x 进行维护检查。如果电站 x 在线，则它自行解决检查。如果电站 x 已离线，则检查由与 x 同一 电网 中 编号最小 的在线电站解决。如果该电网中 不存在 任何 在线 电站，则返回 -1。
# [2, x]：电站 x 离线（即变为非运行状态）。
# 返回一个整数数组，表示按照查询中出现的顺序，所有类型为 [1, x] 的查询结果。
# 注意：电网的结构是固定的；离线（非运行）的节点仍然属于其所在的电网，且离线操作不会改变电网的连接性。
#
# 用并查集来维护同一电网的电站。为每个电网建立最小堆。电站离线的时候只记录状态不修改堆，当需要查询的时候再检查堆顶是否离线，如果离线就更新堆。
class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        stations = [v for v in range(c + 1)]
        poweron = [True] * (c + 1)

        def getparent(id):
            parent = stations[id]
            while stations[parent] != parent:
                parent = stations[parent]
            p = id
            while stations[p] != p:
                t = stations[p]
                stations[p] = parent
                p = t
            return parent

        def connect(i, j):
            parenti = getparent(i)
            parentj = getparent(j)
            if parenti < parentj:
                stations[parentj] = parenti
            else:
                stations[parenti] = parentj

        for u, v in connections:
            connect(u, v)

        powernet = dict()
        for i in range(1, c + 1):
            parent = getparent(i)
            if parent not in powernet:
                powernet[parent] = [i]
            else:
                heappush(powernet[parent], i)

        # print(powernet)
        # print(stations)
        res = []
        for op, val in queries:
            # print(f"{op}, {val}")
            if op == 1:
                if poweron[val]:
                    res.append(val)
                else:
                    pnet = powernet[stations[val]]
                    while pnet and not poweron[pnet[0]]:
                        heappop(pnet)
                    if len(pnet) == 0:
                        res.append(-1)
                    else:
                        res.append(pnet[0])
            elif op == 2 and poweron[val]:
                poweron[val] = False
                # print(powernet)
        return res


if __name__ == "__main__":
    solution = Solution()
    c = 3
    connections = [[2,3],[1,2],[1,3]]
    queries = [[1,1],[1,2],[1,2],[1,3],[1,3],[1,1],[2,3],[1,1],[2,2],[2,2],[1,2],[1,3],[2,1],[2,1],[1,3],[2,1],[2,3],[1,3],[1,3],[2,2],[1,1],[2,2],[1,2],[1,1],[1,2],[1,3],[1,2],[1,3],[2,2],[2,2],[2,3],[1,3],[1,2],[2,3],[1,2],[2,3],[2,3],[2,2],[2,2],[1,1],[2,3],[1,1]]
    print(solution.processQueries(c, connections, queries))  # [1,2,2,3,3,1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]