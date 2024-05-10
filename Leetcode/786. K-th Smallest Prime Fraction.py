class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        q = []

        # store the smallest possible fraction for each element as a numerator in a heap
        for i in range(n-1):
            heapq.heappush(q, (arr[i]/arr[-1], i, n-1))
        
        while k - 1:
            # pop the smallest of the smallest set stored in the heap
            _, i, j = heapq.heappop(q)

            # push the nest smallest fraction with that element as the numerator
            if i < j - 1:
                heapq.heappush(q, (arr[i] / arr[j - 1], i, j - 1))
            
            # do this k-1 times
            k -= 1
        
        # return the smallest fraction
        return [arr[q[0][1]], arr[q[0][2]]]