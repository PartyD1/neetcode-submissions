# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #root is the top. root doesnt move
        #swap left and rights and then move down. if that exists, swap that. 
        if not root:
            return None
        
        root.left, root.right = root.right, root.left

        #use tuple unboxing to switch without a temp var

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
        