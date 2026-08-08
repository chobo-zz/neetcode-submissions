class Solution:
    def compress(self, chars: List[str]) -> int:
        write, read = 0, 0

        while read < len(chars):
            chars[write] = chars[read]
            write += 1

            j = read + 1
            while j < len(chars) and chars[j] == chars[read]:
                j += 1
            
            if (j - read) > 1:
                for c in str(j - read):
                    chars[write] = c
                    write += 1
            read = j
        
        return write

    # [a, a, b]
            
