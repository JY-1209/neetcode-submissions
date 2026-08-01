# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur_head = nth_node_from_end = head

        for _ in range(n):
            cur_head = cur_head.next

        if not cur_head:
            return nth_node_from_end.next
        
        while cur_head.next:
            cur_head = cur_head.next
            nth_node_from_end = nth_node_from_end.next

        nth_node_from_end.next = nth_node_from_end.next.next
        
        return head
