class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        if beginWord == endWord:
            return 0
        wordList.append(beginWord)
        
        q = deque([beginWord])
        adjList = defaultdict(list)
        visited = set([beginWord])

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                adjList[pattern].append(word)
        
        transformations = 1
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return transformations
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i + 1:]
                    for nextWord in adjList[pattern]:
                        if nextWord not in visited:
                            q.append(nextWord)
                            visited.add(nextWord)
            transformations += 1

        
        return 0