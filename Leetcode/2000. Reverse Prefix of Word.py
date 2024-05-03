class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        # find first occurence of character
        for i in range(len(word)):
            if word[i] == ch:

                # if character found, reverse word based on character position
                prefix = word[0:i + 1][::-1]
                try:
                    word = prefix + word[i + 1:]
                except:
                    pass

                break

        
        #return character based reversed word
        return word