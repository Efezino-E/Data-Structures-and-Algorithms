class Solution:
    def minOperations(self, nums, k) -> int:
        # keep track of number of operations 0
        num_ops = 0

        # sort the list by pushing it in a heap
        import heapq
        heapq.heapify(nums)

        # While True (since we are certain the operation must terminate)
        while True:
            # peek at the smallest element
            smallest = nums[0]

            # if smallest element is greater than k, 
            # return number of operations
            if smallest >= k:
                return num_ops

            # else perform the operation
            else:
                s1 = heapq.heappop(nums)
                s2 = heapq.heappop(nums)
                val = 2 * s1 + s2
                heapq.heappush(nums, val)
                num_ops += 1