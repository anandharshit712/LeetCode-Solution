class Solution:
    def compress(self, chars: List[str]) -> int:
        write_index = 0
        read_index = 0
        while read_index < len(chars):
            char = chars[read_index]
            count = 0
            while read_index < len(chars) and chars[read_index] == char:
                count += 1
                read_index += 1
            chars[write_index] = char
            write_index += 1
            if count > 1:
                for digit in str(count):
                    chars[write_index] = digit
                    write_index += 1
        while len(chars) > write_index:
            chars.pop()
        return write_index