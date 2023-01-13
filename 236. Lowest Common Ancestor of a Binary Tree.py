# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    class Searcher:
        def __init__(self, curr, prev = None, level = 0):
            self.curr = curr
            self.prev = prev
            self.level = level

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        found = []
        def find(node, targets, prev = None, level = 0):
            nonlocal found
            searcher = self.Searcher(node, prev, level)
            if node.val in targets:
                found += [searcher]
            
            if len(found) == 2:
                return

            if node.left != None: find(node.left, targets, searcher, level + 1)
            if node.right != None: find(node.right, targets, searcher, level + 1)


        find(root, {p.val, q.val})

        while found[0].level > found[1].level:
            found[0] = found[0].prev

        while found[1].level > found[0].level:
            found[1] = found[1].prev

        while found[0].curr.val != found[1].curr.val:
            found[0], found[1] = found[0].prev, found[1].prev

        return found[0].curr