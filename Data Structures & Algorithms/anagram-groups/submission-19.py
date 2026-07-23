class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_dict = defaultdict(list)
        for s in strs:
            sorted_dict[''.join(sorted(s))].append(s)
        return list(sorted_dict.values())
        
        