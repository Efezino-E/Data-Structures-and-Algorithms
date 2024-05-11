class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        # calaulate rate and sort the workers according to their ratio
        # while still storing their quality
        store = []
        for i in range(len(quality)):
            store.append((wage[i] / quality[i], quality[i]))
        
        store.sort(key = lambda p:p[0])

        # create a max heap to store pairs based on their quality
        # keep track of the total quality you have to pay for in everyone
        qualityHeap = []
        total_quality = 0
        pay = float("inf")

        for rate, q in store: # the current rate is always the maximum rate so far as we have previously sorted
            heapq.heappush(qualityHeap, -q)
            total_quality += q

            # if we have selected more than enough workers, since we are at the maximum rate, we will have to remove the maximum quality experienced so far
            # if the quality removed the quality of the corresponding rate, since the previous rate was lesser, we still pick the minimum
            # in order words, we need to keep track of the minimum
            if len(qualityHeap) > k:
                total_quality += heapq.heappop(qualityHeap)
            
            if len(qualityHeap) == k:
                pay = min(pay, rate * total_quality)
        
        return pay
