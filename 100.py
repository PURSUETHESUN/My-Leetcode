# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        flag = True
        def check(p:TreeNode,q:TreeNode):
            nonlocal flag
            if not p and not q:
                return
            elif not p or not q:
                flag = False
                return
            elif p.val != q.val:
                flag = False
                return
            else:
                check(p.left,q.left)
                check(p.right,q.right)
        check(p,q)
        return flag