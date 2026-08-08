class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # topological sort (DAG) -> dfs with postorder processing
            # add char to result after we have traversed all of node's edges, 
            # then return result in reverse order
        # build adjacency list
        # keep track of visiting (cycles) and visited (avoid re-processing)

        visiting = set()
        visited = set()
        adj = { c: [] for word in words for c in word } # adj[c] = [letters ordered after c]
        res = []

        # scan through list and build adjacency list
        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]

            # handle case where same prefix but len(w1) > len(w2) -> return "" immediately
            minLength = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLength] == w2[:minLength]:
                return ""
            
            # else, find the first differing character between two strings and build adj list
            for j in range(minLength):
                if w1[j] != w2[j]:
                    adj[w1[j]].append(w2[j])
                    break
        
        def dfs(c):
            # cycle detected
            if c in visiting:
                return False
            
            # avoid reprocessing
            if c in visited:
                return True
            
            visiting.add(c)

            for nei in adj[c]:
                if not dfs(nei):
                    return False
            
            visiting.remove(c)
            visited.add(c)

            # we exhausted all paths, so we can now add this character to our result
            res.append(c)
            return True

        # possible the graphs are disconnected, so run dfs on each node
        for c in adj:
            if not dfs(c):
                return ""
        return "".join(reversed(res))
        
            
