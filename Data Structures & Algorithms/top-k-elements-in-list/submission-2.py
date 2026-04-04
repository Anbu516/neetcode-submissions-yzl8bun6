class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in range(len(nums)):
            d[nums[i]]=1+d.get(nums[i],0)
        l=[]
        for n,c in d.items():
            l.append([c,n])
        l.sort()

        res = []
        while len(res)<k:
            res.append(l.pop()[1])
        return res