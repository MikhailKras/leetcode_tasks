class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        letters = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        res_set = set()
        for word in words:
            morse_word = ''
            for letter in word:
                morse_word += letters[ord(letter) - 97]
            res_set.add(morse_word)
        return len(res_set)

