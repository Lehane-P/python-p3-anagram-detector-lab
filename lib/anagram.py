# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, word_list):
        
        word = self.word.lower()

        
        anagrams = [w for w in word_list if self.is_anagram(word, w.lower())]

        
        anagrams = [w for w in anagrams if w != self.word.lower()]

        return anagrams

    @staticmethod
    def is_anagram(word1, word2):
       
        return sorted(word1) == sorted(word2)


# test case
listen = Anagram("listen")
matches = listen.match(['enlists', 'google', 'inlets', 'banana'])

print(matches) 
