# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Node:
    def __init__(self, node) -> None:
        self.node = node
    def __lt__(self, other):
        return self.node.val < other.node.val
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heaps = []
        curr = res = ListNode()
        for l in lists:
            if l :
                heapq.heappush(heaps, Node(l))
        while heaps:
            temp = heapq.heappop(heaps)
            curr.next = temp.node
            curr = curr.next

            if temp.node.next:
                heapq.heappush(heaps, Node(temp.node.next))
        return res.next
        
        print(heaps)
