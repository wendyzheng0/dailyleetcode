from typing import List

###
# 给定两个稀疏向量，计算它们的点积（数量积）。
# 实现类 SparseVector：
# SparseVector(nums) 以向量 nums 初始化对象。
# dotProduct(vec) 计算此向量与 vec 的点积。
# 稀疏向量 是指绝大多数分量为 0 的向量。你需要 高效 地存储这个向量，并计算两个稀疏向量的点积。
# 进阶：当其中只有一个向量是稀疏向量时，你该如何解决此问题？
# 似乎用什么方式做都差不多，还是C++更快一点。
class SparseVector:
    def __init__(self, nums: List[int]):
        self.value = []
        for i, v in enumerate(nums):
            if v != 0:
                self.value.append((i, v))

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        j = res = 0
        n = len(vec.value)
        for i, v in self.value:
            while j < n and vec.value[j][0] < i:
                j += 1
            if j >= n:
                break
            if i == vec.value[j][0]:
                res += v * vec.value[j][1]
        return res
    
class SparseVector2:
    def __init__(self, nums: List[int]):
        self.value = dict()
        for i, v in enumerate(nums):
            if v != 0:
                self.value[i] = v

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        for key in self.value.keys():
            if key in vec.value:
                res += self.value[key] * vec.value[key]
        return res