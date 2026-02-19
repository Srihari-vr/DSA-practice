# brute force
# just traverse the array completly twice to find two pairs 

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range (len(nums)):
            for j in range (i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return i,j
                
# using hashmap 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp={} #val : idx
        for i , n in enumerate(nums):
            diff = target-n
            if diff in mp:
                return [mp[diff],i]:
            
            

