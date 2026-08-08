class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        if len(words) < 2:
            return words[0]
        adj = { c: [] for word in words for c in word }

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]

            minLength = min(len(w1), len(w2))

            if w1[:minLength] == w2[:minLength] and len(w1) > len(w2):
                return ""
            
            for j in range(minLength):
                if w1[j] != w2[j]:
                    adj[w1[j]].append(w2[j])
                    break
        
        visiting = set()
        visited = set()
        res = []

        def dfs(char):
            if char in visiting:
                return False

            if char in visited:
                return True
            
            visiting.add(char)

            for nei in adj[char]:
                if not dfs(nei):
                    return False
            
            visiting.remove(char)
            visited.add(char)
            res.append(char)
            return True
        
        for c in adj:
            if not dfs(c):
                return ""
        res.reverse()
        return "".join(res)
        
        

                
