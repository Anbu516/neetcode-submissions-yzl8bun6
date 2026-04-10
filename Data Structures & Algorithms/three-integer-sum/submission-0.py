class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        l1 = [ ]
        for k in range(len(nums)):
            if k>0 and nums[k]==nums[k-1]:
                continue
            target = nums[k]
            l,r=k+1,len(nums)-1
            while l<r:
                value=target+nums[l]+nums[r]
                if value<0:
                    l+=1
                elif value>0:
                    r-=1
                else:
                    l1.append([nums[k],nums[l],nums[r]])
                    l+=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
        return l1