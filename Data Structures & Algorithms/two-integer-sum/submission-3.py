class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return [sorted([idx_i, idx_j]) for idx_i, i in enumerate(nums) for idx_j, j in enumerate(nums) if idx_i != idx_j and i + j == target][0]