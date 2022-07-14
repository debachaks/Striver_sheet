#Using Dictionary, TC: O(n), SC: O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        dictionary = {}
        for i in range(n):
            if (target-nums[i]) in dictionary.keys():
                return i,dictionary[(target-nums[i])]
            dictionary[nums[i]] = i
    
