# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def length(node):
        if (not node): 
            return 0
        else:
            return 1 + length(node.next)
class Solution:
    
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = length(head)
        middle_node = n // 2

        if not head:
            return
        if middle_node == 0:
            head = head.next
            return
        curr = head
        count = 0
        while curr and count < middle_node - 1:
            curr = curr.next
            count += 1
        if not curr or not curr.next:
            return
        curr.next = curr.next.next

        return head
        