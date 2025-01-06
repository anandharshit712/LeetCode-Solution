class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        operations = [0] * n

    # Left-to-right pass
        left_balls = 0
        left_cost = 0
        for i in range(n):
            operations[i] += left_cost
            if boxes[i] == '1':
                left_balls += 1
            left_cost += left_balls

    # Right-to-left pass
        right_balls = 0
        right_cost = 0
        for i in range(n - 1, -1, -1):
            operations[i] += right_cost
            if boxes[i] == '1':
                right_balls += 1
            right_cost += right_balls

        return operations