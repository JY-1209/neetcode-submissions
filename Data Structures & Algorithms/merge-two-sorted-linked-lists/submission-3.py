# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list1_ptr = list1
        list2_ptr = list2

        root = copy = ListNode()

        while list1_ptr and list2_ptr:
            if list1_ptr.val <= list2_ptr.val:
                root.next = list1_ptr
                root = root.next
                list1_ptr = list1_ptr.next
            else:
                root.next = list2_ptr
                root = root.next
                list2_ptr = list2_ptr.next
        
        root.next = list1_ptr or list2_ptr
        
        return copy.next