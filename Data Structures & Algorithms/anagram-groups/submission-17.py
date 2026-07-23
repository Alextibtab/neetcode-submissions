class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_dict = {}
        for s in strs:
            sorted_key = ''.join(sorted(s))
            if sorted_key in sorted_dict:
                sorted_dict[sorted_key].append(s)
            else:
                sorted_dict[sorted_key] = [s]
        return list(sorted_dict.values())
        
        