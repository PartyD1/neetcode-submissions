# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        prevNode = None
        first = list1
        second = list2

        while first or second:
            #as long as at least one of them isn't at the end the loop will run:
            if not first:
                if not head:
                    head = second
                    prevNode = second
                    second = second.next
                    
                else:
                    prevNode.next = second
                    prevNode = second
                    second = second.next

                #automaticcaly add 2nd to the list

            elif not second:
                if not head:
                    head = first
                    prevNode = first
                    first = first.next
                else:
                    prevNode.next = first
                    prevNode = first
                    first = first.next
            

            elif first.val <= second.val:
                if not head:
                    head = first
                    prevNode = first
                    first = first.next
                else: 
                    prevNode.next = first
                    prevNode = first
                    first = first.next

            else:
                if not head:
                    head = second
                    prevNode = second
                    second = second.next
                else:
                    prevNode.next = second
                    prevNode = second
                    second = second.next

        return head
        