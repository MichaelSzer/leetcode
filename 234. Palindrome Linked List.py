# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # reverse linked list
        reverse_head, reverse_next_node = ListNode(head.val, head.next), None
        while reverse_head != None:
            if reverse_head.next != None:
                original_next_node = ListNode(reverse_head.next.val, reverse_head.next.next) 
            else: original_next_node = None
            reverse_head.next = reverse_next_node
            reverse_next_node = reverse_head
            reverse_head = original_next_node

        # check all nodes are the same
        reverse_head = reverse_next_node
        while reverse_head != None:
            if reverse_head.val != head.val:
                
                return False
            else:
                reverse_head, head = reverse_head.next, head.next
        
        return True