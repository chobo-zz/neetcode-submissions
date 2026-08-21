class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        num1 = num1[::-1]
        num2 = num2[::-1]
        res = [0] * (len(num1) + len(num2))

        for i in range(len(num1)):
            for j in range(len(num2)):
                product = int(num1[i]) * int(num2[j])

                res[i + j] += product
                res[i + j + 1] += res[i + j] // 10
                res[i + j] = res[i + j] % 10
        
        i = 0
        res = res[::-1]
        while i < len(res) and res[i] == 0:
            i += 1
        res = res[i:]
        res = map(str, res)
        return "".join(res)
