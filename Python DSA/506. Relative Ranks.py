class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        # map the position of each score
        position_mapping = self.position(score)
        print(position_mapping)

        # create a new array for medals
        medals = []

        # Give medals to the score based on position mapping
        for i in score:
            print
            if position_mapping[i] == 0:
                medals.append("Gold Medal")
            elif position_mapping[i] == 1:
                medals.append("Silver Medal")
            elif position_mapping[i] == 2:
                medals.append("Bronze Medal")
            else:
                medals.append(str(position_mapping[i] + 1))
        
        return medals
    
    def position(self, arr):
        # sort the array
        arr = sorted(arr, reverse = True)

        # map the unique elements in the array to their position
        position_mapping = {}
        for i in range(len(arr)):
            position_mapping[arr[i]] = i

        return position_mapping