class Solution(object):
    def equalSubstring(self, s, t, maxCost):
        # use a sliding window to find the optimal substring
        curCost = 0
        l = 0
        maxWindow = 0

        for r in range(len(s)):
            curCost += abs(ord(s[r]) - ord(t[r]))

            while curCost > maxCost:
                curCost -= abs(ord(s[l]) - ord(t[l]))
                l += 1
            
            maxWindow = max(maxWindow, r - l + 1)
        
        return maxWindow