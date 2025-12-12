from typing import List


###
# 给你一个整数 numberOfUsers 表示用户总数，另有一个大小为 n x 3 的数组 events 。
# 每个 events[i] 都属于下述两种类型之一：
# 消息事件（Message Event）：["MESSAGE", "timestampi", "mentions_stringi"]
# 事件表示在 timestampi 时，一组用户被消息提及。
# mentions_stringi 字符串包含下述标识符之一：
# id<number>：其中 <number> 是一个区间 [0,numberOfUsers - 1] 内的整数。可以用单个空格分隔 多个 id ，并且 id 可能重复。此外，这种形式可以提及离线用户。
# ALL：提及 所有 用户。
# HERE：提及所有 在线 用户。
# 离线事件（Offline Event）：["OFFLINE", "timestampi", "idi"]
# 事件表示用户 idi 在 timestampi 时变为离线状态 60 个单位时间。用户会在 timestampi + 60 时自动再次上线。
# 返回数组 mentions ，其中 mentions[i] 表示  id 为  i 的用户在所有 MESSAGE 事件中被提及的次数。
# 最初所有用户都处于在线状态，并且如果某个用户离线或者重新上线，其对应的状态变更将会在所有相同时间发生的消息事件之前进行处理和同步。
# 注意 在单条消息中，同一个用户可能会被提及多次。每次提及都需要被 分别 统计。
#
# 模拟，注意细节。
class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        events.sort(key=lambda x: (int(x[1]), 0 if x[0] == 'OFFLINE' else 1))
        offline = [False] * numberOfUsers
        onlineque = []
        mentions = [0] * numberOfUsers
        mentionall = 0
        for msgtype, time, mentionstr in events:
            time = int(time)
            while onlineque and onlineque[0][1] <= time:
                offline[onlineque[0][0]] = False
                del onlineque[0]
            if msgtype == 'OFFLINE':
                u = int(mentionstr)
                onlineque.append((u, time + 60))
                offline[u] = True
            else:
                if 'ALL' in mentionstr:
                    mentionall += 1
                elif 'HERE' in mentionstr:
                    for u in range(numberOfUsers):
                        if not offline[u]:
                            mentions[u] += 1
                for u in [v for v in mentionstr.split(' ') if v != 'ALL' and v != 'HERE']:
                    mentions[int(u[2:])] += 1
        for u in range(numberOfUsers):
            mentions[u] += mentionall
        return mentions
