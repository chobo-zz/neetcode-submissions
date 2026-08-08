class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        res = []

        def dfs(i, cur): # return all possible ways to make up letter combinations starting at index i with current character list cur
            if i >= len(digits):
                res.append("".join(cur))
                return
            
            for char in digitToChar[digits[i]]:
                cur.append(char)
                dfs(i + 1, cur)
                cur.pop()
        
        dfs(0, [])
        return res
