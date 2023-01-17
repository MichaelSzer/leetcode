# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, node = None, head
        while node != None:
            # check if duplicated
            if node.next != None and node.val == node.next.val:
                node_to_delete = node.next
                while node != None and node.val == node_to_delete.val:
                    node = node.next

                # check if the node is in front of the list
                if prev != None:
                    prev.next = node
                else:
                    head = node

            # if it's unique just move to the next node
            else:
                prev = node
                node = node.next
        
        return head