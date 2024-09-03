# Tries-1

## Problem 1 Implement Trie (Prefix Tree)(https://leetcode.com/problems/implement-trie-prefix-tree/)

class Trie:
    class TrieNode:
        def __init__(self):
            self.children = [None for i in range(26)]
            self.isEnd = False

    def __init__(self):
        self.root = self.TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for i in range(len(word)):
            c = word[i]
            if curr.children[ord(c) - ord('a')] == None:
                curr.children[ord(c) - ord('a')] = self.TrieNode()
            curr = curr.children[ord(c) - ord('a')]
        curr.isEnd = True
        
    def search(self, word: str) -> bool:
        curr = self.root
        for i in range(len(word)):
            c = word[i]
            if curr.children[ord(c) - ord('a')] == None:
                return False
            curr = curr.children[ord(c) - ord('a')]
        return curr.isEnd
        
    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for i in range(len(prefix)):
            c = prefix[i]
            if curr.children[ord(c) - ord('a')] == None:
                return False
            curr = curr.children[ord(c) - ord('a')]
        return True
        
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

## Problem 2 Longest Word in Dictionary(https://leetcode.com/problems/longest-word-in-dictionary/)

class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort(key=len)  # sort words by non-decreasing length
        goodWords = set()  # lookup for good words
        maxLength = 0
        ans = ""
        for word in words:
            if len(word) == 1:
                goodWords.add(word)
            elif word[:-1] in goodWords:  # word with length - 1 prefix is good
                goodWords.add(word)
            if word in goodWords:
                if maxLength < len(word):  # find longer word
                    maxLength = len(word)
                    ans = word
                elif maxLength == len(word):  # find lexicographically smaller word
                    ans = min(ans, word)
        return ans

## Problem 3 Replace Words (https://leetcode.com/problems/replace-words/)

class Solution:
    class TrieNode:
        def __init__(self):
            self.children = [None for i in range(26)]
            self.isEnd = False

    def insert(self, word: str) -> None:
        curr = self.root
        for i in range(len(word)):
            c = word[i]
            if curr.children[ord(c) - ord('a')] == None:
                curr.children[ord(c) - ord('a')] = self.TrieNode()
            curr = curr.children[ord(c) - ord('a')]
        curr.isEnd = True
    
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        if sentence == None or len(sentence) == 0:
            return sentence
        self.root = self.TrieNode()
        for word in dictionary:
            self.insert(word)
        splitArray = sentence.split(" ")
        result = []
        for i in range(len(splitArray)):
            word = splitArray[i]
            replacement = []
            curr = self.root
            for j in range(len(word)):
                c = word[j]
                if curr.children[ord(c) - ord('a')] == None or curr.isEnd == True:
                    break
                replacement.append(c)
                curr = curr.children[ord(c) - ord('a')]
            if curr.isEnd == True:
                result.append("".join(replacement))
            else:
                result.append(word)
        return " ".join(result)
