from typing import List


###
# 给你一个整数 n ，表示有 n 个专家从 0 到 n - 1 编号。另外给你一个下标从 0 开始的二维整数数组 meetings ，其中 meetings[i] = [xi, yi, timei] 表示专家 xi 和专家 yi 在时间 timei 要开一场会。一个专家可以同时参加 多场会议 。最后，给你一个整数 firstPerson 。
# 专家 0 有一个 秘密 ，最初，他在时间 0 将这个秘密分享给了专家 firstPerson 。接着，这个秘密会在每次有知晓这个秘密的专家参加会议时进行传播。更正式的表达是，每次会议，如果专家 xi 在时间 timei 时知晓这个秘密，那么他将会与专家 yi 分享这个秘密，反之亦然。
# 秘密共享是 瞬时发生 的。也就是说，在同一时间，一个专家不光可以接收到秘密，还能在其他会议上与其他专家分享。
# 在所有会议都结束之后，返回所有知晓这个秘密的专家列表。你可以按 任何顺序 返回答案。
#
# 开始的时候准备每个时间开的会都用一个并查集来记录，然后一次次更新，结果超时了。后来就改为只用一个并查集。按照会议时间遍历会议，同一个时间段参加会议的专家更新并查集，
# 处理完一个时间段后只保留0所在的并查集，其他专家重设为原始值。由于专家数量远远大于某一个时间点参加会议的专家数量，每次更新并查集和重设的时候只需要更新这个时间参加过会议的专家。
class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        def getparent(arr, x):
            if arr[x] == x:
                return x
            arr[x] = getparent(arr, arr[x])
            return arr[x]

        def connect(arr, x, y):
            px = getparent(arr, x)
            py = getparent(arr, y)
            if px < py:
                arr[py] = px
            else:
                arr[px] = py

        meetings.sort(key=lambda x: x[2])
        arr = [i for i in range(n)]
        arr[firstPerson] = 0
        cur = 0
        for idx, [x, y, time] in enumerate(meetings):
            if time != meetings[cur][2]:
                # switch to new time
                for i in range(cur, idx):
                    xx, yy, _ = meetings[i]
                    if getparent(arr, xx) != 0:
                        arr[xx] = xx
                    if getparent(arr, yy) != 0:
                        arr[yy] = yy
                cur = idx
            connect(arr, x, y)

        res = []
        for i in range(n):
            if getparent(arr, i) == 0:
                res.append(i)
        return res
