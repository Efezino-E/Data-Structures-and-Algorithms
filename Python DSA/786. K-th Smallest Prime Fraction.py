class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        l = 0
        r = 1
        n = len(arr)

        # perform a binary search over the range of 0 to 1
        while l < r:
            m = (l + r)/2 
            # keep track of how many valid paris of fractions are below the current m
            cnt = 0
            j = 1
            # keep track of the fraction pair closest to  the current m
            maxF =  0

            for i in range(n - 1):
                while j < n:
                    if arr[i] / arr[j] > m:
                        j += 1
                    else:
                        cnt += n - j
                        if arr[i] / arr[j] > maxF:
                            p = i
                            q = j
                            maxF = arr[i] / arr[j]
                        break
            # update the binary search based on count of elements less than m and return when equal to k
            if cnt > k:
                r = m
            elif cnt < k:
                l = m
            else:
                return arr[p], arr[q]
