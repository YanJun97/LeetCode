import collections
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        table = collections.defaultdict(list)
        for i in range(len(nums)):
            table[nums[i]].append(i)
        for key in table:
            if target - key in table:
                if target - key == key:
                    if len(table[key])==2: return table[key][0],table[key][1]
                else: return table[key][0], table[target-key][0]
                
