# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: # check if p and q are empty trees
            return True
        if not p or not q or p.val != q.val: # check if one of the tree is null
            return False

        return (self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right))