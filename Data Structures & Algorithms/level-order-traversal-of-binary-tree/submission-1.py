# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #queue 
        #level - figure out that its a level initialize a new list in the list. 
        #each level will be 2x the previous level
        #save the length of the queue to figure out when each level starts
        if not root:
            return []
        result = []
        q = deque()

        q.append(root)
        lastLen = 0

        while q:
            lastLen = len(q)
            inside = []
            for i in range(lastLen):
                lastNode = q.popleft()
                if lastNode:
                    q.append(lastNode.left)
                    q.append(lastNode.right)
                    inside.append(lastNode.val)
            if inside:
                result.append(inside)

        return result

        

        
