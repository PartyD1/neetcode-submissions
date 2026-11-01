# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])
        split = -1

        #find the root in inorder
        for i in range(len(inorder)):
            if root.val == inorder[i]:
                split = i
                break
                
        preLen = split

        root.left = self.buildTree(preorder[1:preLen+1], inorder[0:split])
        root.right = self.buildTree(preorder[preLen+1:], inorder[split+1:])
        return root

