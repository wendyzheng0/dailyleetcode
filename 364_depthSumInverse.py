from typing import List


###
# 给你一个整数嵌套列表 nestedList ，每一个元素要么是一个整数，要么是一个列表（这个列表中的每个元素也同样是整数或列表）。
# 整数的 深度 取决于它位于多少个列表内部。例如，嵌套列表 [1,[2,2],[[3],2],1] 的每个整数的值都等于它的 深度 。令 maxDepth 是任意整数的 最大深度 。
# 整数的 权重 为 maxDepth - (整数的深度) + 1 。
# 将 nestedList 列表中每个整数先乘权重再求和，返回该加权和。
#
# 先计算最大深度再计算值。后来发现还有更优的算法，就是按层计算，每算下一层就先加上之前算的各层的和，这样就不必计算最大深度了。
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        def getdepth(nestedList):
            res = 0
            for item in nestedList:
                val = item.getList()
                if val is None:
                    res = max(res, 1)
                else:
                    res = max(res, getdepth(val) + 1)
            return res

        maxdepth = getdepth(nestedList)
        # print(f"depth is {maxdepth}")

        def getvalue(nestedList, depth):
            res = 0
            for item in nestedList:
                if item.isInteger():
                    res += item.getInteger() * (maxdepth - depth)
                else:
                    res += getvalue(item.getList(), depth + 1)
            # print(f"{nestedList}: {res}")
            return res
        
        return getvalue(nestedList, 0)
