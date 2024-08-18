class Solution:
    def nthUglyNumber(self, n: int) -> int:
        
        # Create set to store encountered numbers
        # use a heap to keep track of the next ugly number
        # use a for loop to create possible next ugly numbers
        # run the loop for n iterations to obtain the nth ugly number
        
        import heapq
        ugly_numbers = [1]
        min_heap = []
        store = set([1])

        for i in range(n - 1):
            j = ugly_numbers[-1]
            for k in [2, 3, 5]:
                to_push = k * j
                if to_push not in store:
                    heapq.heappush(min_heap, to_push)
                    store.add(to_push)

            to_add = heapq.heappop(min_heap)
            ugly_numbers.append(to_add)
        
        return ugly_numbers[-1]