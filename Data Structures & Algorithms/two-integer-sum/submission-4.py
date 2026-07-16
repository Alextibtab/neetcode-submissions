class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return next(([nums.index(target - num), i] for i, num in enumerate(nums) if target - num in nums[:i]), [])
