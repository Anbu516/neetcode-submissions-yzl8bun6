class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap=defaultdict(list)
        for s in strs:
            srtd_str=''.join(sorted(s))
            hashmap[srtd_str].append(s)
        return list(hashmap.values())