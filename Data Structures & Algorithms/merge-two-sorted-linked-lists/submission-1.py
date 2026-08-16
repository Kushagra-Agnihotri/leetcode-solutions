# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp = new = ListNode()

        while l1 and l2:
            print(l1.val, l2.val)
            if l1.val > l2.val:
                new.next = ListNode(l2.val)
                l2 = l2.next

            else:
                new.next = ListNode(l1.val)
                l1 = l1.next
            new = new.next
        if l2:
            while l2:
                new.next = ListNode(l2.val)
                l2 = l2.next
                new = new.next
        else:
            while l1:
                new.next = ListNode(l1.val)
                l1 = l1.next
                new = new.next
        return temp.next
