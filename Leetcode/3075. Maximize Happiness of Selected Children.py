class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        # select the happiest children (so sort the array)
        happiness.sort(reverse = True)

        # pick k children and reduce happiness on each count
        # their happiness cannot be less than 0
        satisfied = 0
        for i in range(k):
            satisfied += max(happiness[i] - i, 0)
        
        return satisfied