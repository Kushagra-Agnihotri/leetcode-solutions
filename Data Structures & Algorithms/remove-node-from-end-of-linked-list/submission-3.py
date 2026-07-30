# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 0
        if not head: return 
        cur = head 
        while cur:
            cur = cur.next
            l+=1
        index = l-n

        if index == 0 :
            return head.next

        cur = head
        for i in range(l-1):
            if (i+1) == index:
                cur.next = cur.next.next
                break
            cur= cur.next
        return head