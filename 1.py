class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # n = dict(zip(nums,range(len(nums))))  when meets [3,3] go wrong
        n = {}
        for x in range(len(nums)):
            if n.get(target-nums[x]) == None:
                n[nums[x]] = x
            else:
                return [n.get(target-nums[x]),x]

a = Solution()

print(a.twoSum([1,4,45,2356,264535,2334,6565,34,34,254,432,234,6545643,235,3,6],10))
