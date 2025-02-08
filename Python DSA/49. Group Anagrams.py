class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Key is a dictionary mapping of unique anagram groups
        # to the index of the group's list in the larger final list "ans"
        # A sorted string of the anagram is used as the unique key (this can be imporved)
        key = {}
        ans = []

        # i stores the index of the angram group in the order in which they are discovered
        i = 0

        # iterate through every word
        # generate it's unique key
        # check if the key is already mapped to an index 
        # if already mapped, add the word to its group
        # if not mapped, created a group of just that word
        #  and then increase the index i to store the next new group discovered as a new group
        for word in strs:
            p_key = "".join(sorted(word))
            if p_key in key:
                ans[key[p_key]].append(word)
            else:
                key[p_key] = i
                ans.append([word])
                i += 1
        return ans       