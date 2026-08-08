class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        dtc = { 
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
        cur = []

        def dfs(i):
            if i == len(digits):
                res.append("".join(cur))
                return
            
            for letter in dtc[digits[i]]:
                cur.append(letter)
                dfs(i + 1)
                cur.pop()
            
        dfs(0)
        return res
