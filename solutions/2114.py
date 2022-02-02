# Maximum Number of Words Found in Sentences

from typing import List

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxLen = len(sentences[0].split())
        for i in range(1, len(sentences)):
            maxLen = max(len(sentences[i].split()), maxLen)

        return maxLen

if __name__ == "__main__":
    sol = Solution()
    sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
    sentences = ["please wait", "continue to fight", "continue to win"]
    print(sol.mostWordsFound(sentences))
