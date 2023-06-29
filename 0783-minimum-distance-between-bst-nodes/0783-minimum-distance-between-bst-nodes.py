# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.test=10**5+1
        self.prev=-self.test
        
        def search(node):
            if node==None:
                return
            
            search(node.left)
            self.test=min(self.test,node.val-self.prev)
            self.prev=node.val
            search(node.right)
            
        search(root)
        
        return self.test