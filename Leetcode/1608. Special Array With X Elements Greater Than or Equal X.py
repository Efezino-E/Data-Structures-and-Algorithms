class Solution(object):
    def specialArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # sort the nums array and keep track of the maximum element encountered
        nums.sort()
        passed = -1

        # iterate through the array
        for i in range(len(nums)):
            
            # if the current element is greater than or equal to 
            # the length of the rest of the array that starts with that element
            # and it is greater than every element encourntered, then return
            # the length of the rest of the array that starts with that element
            if nums[i] >= len(nums) - i and len(nums) - i > passed:
                return len(nums) - i

            # update the maximum element encountered
            else:
                passed = max(passed, nums[i])
        
        # return -1 when we didn't find any special elements
        return -1