# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #send a pointer n nodes ahead. keep traversing until the ahead pointer reaches the end. then connect that to 2 pointers ahead of us
        dummy = ListNode(0,head)
        slow = dummy   
        fast = dummy
        for _ in range(n+1):
            fast = fast.next
        #fast is n nodes ahead of slow
        while fast:
            slow = slow.next
            fast = fast.next

        #[1,2,3,4] n= 2
        #next one can be deleted
        slow.next = slow.next.next
        return dummy.next