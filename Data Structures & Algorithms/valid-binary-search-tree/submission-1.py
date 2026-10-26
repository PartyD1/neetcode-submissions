# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        #is the root bigger than left and smaller than right
        #lmight not be a left or right or both. 
        if root.left and root.right:
            #do smt
            if root.left.val < root.val and root.right.val > root.val:
                #recursive call
                return self.isValidBST(root.left) and self.isValidBST(root.right)
            else:
                return False

        #only one side
        if root.left:
            if root.left.val < root.val:
                return self.isValidBST(root.left)
            else:
                return False

        if root.right:
            if root.right.val > root.val:
                return self.isValidBST(root.right)
            else:
                return False

        return True