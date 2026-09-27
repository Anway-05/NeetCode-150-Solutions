from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        dq=deque([beginWord])
        moves=1
        wordSet=set(wordList)
        if beginWord in wordSet:
            wordSet.remove(beginWord)
        while dq:
            moves+=1
            length=len(dq)
            for _ in range(length):
                word=dq.popleft()
                for i in range(len(word)):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        new_word=word[:i]+c+word[i+1:]
                        if new_word in wordSet:
                            wordSet.remove(new_word)
                            if new_word==endWord:
                                return moves
                            dq.append(new_word)
        return 0
            