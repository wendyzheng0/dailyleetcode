from typing import List


###
# 给你一棵 n 个节点的无向树，节点编号为 0 到 n - 1 。给你整数 n 和一个长度为 n - 1 的二维整数数组 edges ，其中 edges[i] = [ai, bi] 表示树中节点 ai 和 bi 有一条边。
# 同时给你一个下标从 0 开始长度为 n 的整数数组 values ，其中 values[i] 是第 i 个节点的 值 。再给你一个整数 k 。
# 你可以从树中删除一些边，也可以一条边也不删，得到若干连通块。一个 连通块的值 定义为连通块中所有节点值之和。如果所有连通块的值都可以被 k 整除，那么我们说这是一个 合法分割 。
# 请你返回所有合法分割中，连通块数目的最大值 。
#
# 开始的时候尝试一根根edge来删，看最大可以删多少条，结果超时了，因为这样求的是全解。看了灵神的题解发现只需要求其中一种就可以了。
# 在深度优先遍历求子树值的时候如果遇到可以被k整除的值时就可以做一次分割。这样的分割有可能因为最开始选择根结点不同而不同，但是分割数似乎是一样的。我没有严格证明。
# 但这样子只需要遍历一次就得到答案了。
class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        res = 0
        g = [[] for _ in range(n)]
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)

        def getValue(node, parent):
            s = values[node]
            for c in g[node]:
                if c != parent:
                    s += getValue(c, node)
            nonlocal res
            if s % k == 0:
                res += 1
            # print(f"node:{node}, parent:{parent}, s:{s}, res:{res}")
            return s
        
        getValue(0, -1)
        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxKDivisibleComponents(n=5, edges=[[0,2],[1,2],[1,3],[2,4]], values=[1,8,1,4,4], k=6)) # 2
    print(solution.maxKDivisibleComponents(n=7, edges=[[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]], values=[3,0,6,1,5,2,1], k=3)) # 3
    print(solution.maxKDivisibleComponents(n=9, edges=[[0,1],[0,5],[1,6],[5,8],[8,4],[8,3],[7,2],[3,7]], values=[10,5,6,15,10,15,5,9,5], k=5)) # 8
    print(solution.maxKDivisibleComponents(n=3, edges=[[0,2],[2,1]], values=[0,0,0], k=1)) # 3
    print(solution.maxKDivisibleComponents(n=10, edges=[[8,1],[5,6],[5,3],[1,5],[2,7],[7,4],[6,4],[4,0],[6,9]], values=[9,27,6,4,0,2,12,3,9,9], k=9)) # 7