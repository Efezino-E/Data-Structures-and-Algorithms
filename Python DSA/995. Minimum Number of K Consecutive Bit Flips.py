class Solution(object):
    def minKBitFlips(self, nums, k):
        from collections import deque
        # start a queue to store indexes that start flips
        q = deque()
        res = 0

        for i in range(len(nums)):
            # remove all indexes whose flips can't affect the current index
            while q and i > q[0] + k - 1:
                q.popleft()

            # flip elements if possible and increment the result and update queue
            if (nums[i] + len(q)) % 2 == 0:
                
                # return ans if impossible
                if i + k > len(nums):
                    return -1

                q.append(i)
                res += 1
        
        # return ans
        return res        