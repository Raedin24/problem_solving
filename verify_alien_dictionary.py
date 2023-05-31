class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        for index in range(len(words) - 1):
            word = words[index]
            next_word = words[index + 1]

            for i in range(len(word)):
                if i >= len(next_word):
                    return False
                if order.index(word[i]) < order.index(next_word[i]):
                    break
                elif order.index(word[i]) > order.index(next_word[i]):
                    return False


        return True              