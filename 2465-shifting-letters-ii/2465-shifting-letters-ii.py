class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        shift_effect = [0] * (n + 1)

        for start, end, direction in shifts:
            if direction == 1:
                shift_effect[start] += 1
                shift_effect[end + 1] -= 1
            else:
                shift_effect[start] -= 1
                shift_effect[end + 1] += 1

        cumulative_shift = 0
        for i in range(n):
            cumulative_shift += shift_effect[i]
            shift_effect[i] = cumulative_shift

        result = []
        for i, char in enumerate(s):
            net_shift = shift_effect[i] % 26
            new_char = chr((ord(char) - ord('a') + net_shift) % 26 + ord('a'))
            result.append(new_char)

        return ''.join(result)