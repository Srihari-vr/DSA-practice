# sorting and then checking if there 2 adjacent indices are the same 
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s_nums=sorted(nums)
        if len(s_nums)==1:
            return False
        for i in range(len(s_nums)-1):
            if s_nums[i]==s_nums[i+1]:
                return True
        return False
    
# using set to see if the value has already appeared 

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset=set()
        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        return False