class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx_i, i in enumerate(nums):
            for idx_j, j in enumerate(nums[1:]):
                if idx_i != idx_j + 1 and i + j == target:
                    return sorted([idx_i, idx_j + 1])