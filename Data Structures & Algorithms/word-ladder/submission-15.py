class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        wordList.append(endWord)
        adjList = defaultdict(list)
        q = deque([beginWord])
        count = 0
        visited = set([beginWord])

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                adjList[pattern].append(word)
        
        while q:
            count += 1

            for _ in range(len(q)):
                word = q.popleft()

                if word == endWord:
                    return count

                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i + 1:]
                    for match in adjList[pattern]:
                        if match not in visited:
                            q.append(match)
                            visited.add(match)
        return 0
                
