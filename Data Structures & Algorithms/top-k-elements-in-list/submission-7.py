class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1
        return [item[0] for item in sorted(counter.items(), key=lambda ele: ele[1], reverse=True)][:k]