class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        # initiate a set and store a maximum number
        p_set = set()
        maxi = -float("inf")

        # iterate through scores in the list and store them
        # check if store has the negative element
        for i in range(len(nums)):
            if nums[i] not in p_set:
                p_set.add(nums[i])

            if -nums[i] in p_set:
                maxi = max(abs(nums[i]), maxi)
        
        if maxi == - float("inf"):
            return -1
        return maxi