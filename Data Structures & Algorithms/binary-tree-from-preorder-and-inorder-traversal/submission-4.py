
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        if not preorder:
            return None

        root = TreeNode(preorder[0])
        split = -1

        for i in range(len(inorder)):
            if root.val == inorder[i]:
                split = i
                break

        

        root.left = self.buildTree(
            preorder[1:split+1],
            inorder[:split]
        )

        root.right = self.buildTree(
            preorder[split+1:],
            inorder[split+1:]
        )

        return root
