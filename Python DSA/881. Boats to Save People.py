class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        num_boats = 0       
        people = sorted(people)
        space_left = limit

        from collections import deque
        people = deque(people)

        while len(people) != 0:
            # take a new boat and check if the heaviest person can be paired
            # remove the heaviest person and the smallest person if the smallest person can fit
            num_boats += 1
            space_left = limit - people.pop()

            if  (len(people) != 0) and (people[0] <= space_left):
                people.popleft()

        return num_boats