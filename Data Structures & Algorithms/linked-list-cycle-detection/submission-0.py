# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        current = head

        while current:
            if current.val in seen:
                return True
            seen.add(current.val)
            current = current.next
            #print("i am here: ", current.val)
        
        return False