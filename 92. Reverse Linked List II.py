# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right: return head

        node, i = head, 1
        while i < left - 1:
            i += 1
            node = node.next
        
        start_node = None if left == 1 else node
        node = node if left == 1 else node.next
        i += 0 if left == 1 else 1

        first_node = node
        prev_node = None
        while i < right:
            i += 1
            next_node = node.next
            node.next = prev_node
            prev_node = node
            node = next_node
        
        # node is the end node, prev_node is the previous to that one
        if start_node == None: head = node
        else: start_node.next = node

        first_node.next = node.next
        node.next = prev_node

        return head