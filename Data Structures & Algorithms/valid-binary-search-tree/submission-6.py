class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def validate(node, lower, upper):
            if not node:
                return True
            
            if not (lower < node.val < upper):
                return False
            
            #if we go left then the node becomes the new upper bound
            #if we go right then the node becomes the new lower bound

            return (validate(node.left, lower, node.val) and validate(node.right, node.val, upper))
        return validate(root, float('-inf'), float("inf"))
    

        