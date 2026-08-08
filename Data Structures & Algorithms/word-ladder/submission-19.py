class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        adj = defaultdict(list)
        q = deque([beginWord])
        visited = set()
        count = 0

        wordList.append(beginWord)

        for i in range(len(wordList)):
            word = wordList[i]

            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                adj[pattern].append(word)
        
        while q:
            count += 1
            for _ in range(len(q)):

                word = q.popleft()

                if word == endWord:
                    return count

                if word in visited:
                    continue
                visited.add(word)
                
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1:]

                    for nei in adj[pattern]:
                        if nei not in visited:
                            q.append(nei)
            
        
        return 0
            
            

