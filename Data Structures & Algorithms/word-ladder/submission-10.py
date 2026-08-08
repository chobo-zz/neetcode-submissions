class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        wordList.append(beginWord)
        adjList = defaultdict(set)
        visited = set([beginWord])
        q = deque([beginWord])
        count = 0

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                adjList[pattern].add(word)
        
        while q:
            count += 1
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return count
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i + 1:]
                    for matchedWord in adjList[pattern]:
                        if matchedWord not in visited:
                            q.append(matchedWord)
                            visited.add(matchedWord)

        return 0
