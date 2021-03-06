'''

Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array

'''
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) ==1:
            return nums[0]
        import collections
        dic = collections.defaultdict(int)
        for val in nums:
            dic[val] += 1
        return sorted(dic, key = lambda x:dic[x])[-1]

            
            
        