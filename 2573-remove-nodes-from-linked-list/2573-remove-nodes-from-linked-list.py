# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head):
            prev = None
            current = head
            while current:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            return prev

        head = reverse(head)

        max_val = float('-inf')
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        current = head

        while current:
            if current.val >= max_val:
                max_val = current.val
                prev = current
            else:
                prev.next = current.next
            current = current.next

        return reverse(dummy.next)