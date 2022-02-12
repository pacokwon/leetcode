# Word Ladder

from typing import List
from queue import Queue

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        wordSet = set(wordList)
        alphabets = 'abcdefghijklmnopqrstuvwxyz'

        q = Queue()
        q.put((beginWord, 1))
        while not q.empty():
            w, num = q.get()

            for i in range(len(w)):
                for a in alphabets:
                    newWord = w[:i] + a + w[i + 1:]

                    if newWord == endWord:
                        return num + 1

                    if newWord in wordSet:
                        wordSet.remove(newWord)
                        q.put((newWord, num + 1))

        return 0

if __name__ == "__main__":
    sol = Solution()
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    beginWord = "leet"
    endWord = "code"
    wordList = ["lest","leet","lose","code","lode","robe","lost"]
    print(sol.ladderLength(beginWord, endWord, wordList))
