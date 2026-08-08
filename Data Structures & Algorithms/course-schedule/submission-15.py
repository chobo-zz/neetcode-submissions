class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visiting = set()        # current recursion stack
        completed = set()       # fully processed nodes

        # pre -> list of courses unlocked after pre
        preToCrs = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preToCrs[pre].append(crs)

        def dfs(pre):
            if pre in visiting:
                return False
            if pre in completed:
                return True
            
            visiting.add(pre)
            for crs in preToCrs[pre]:
                if not dfs(crs):
                    return False
            visiting.remove(pre)
            completed.add(pre)
            
            return True
        
        for pre in range(numCourses):
            if not dfs(pre):
                return False
        return True