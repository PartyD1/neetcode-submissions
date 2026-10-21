from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        sub = defaultdict(list)

        for s in strs:
            sorted_s = tuple(sorted(s))
            #sorted_s = str(sorted_s)
            sub[sorted_s].append(s)
            
        for value in sub.values():
            result.append(value)

        return result

