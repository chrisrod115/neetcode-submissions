# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        SEEN = set()
        CUR = head
        while CUR:
            if CUR in SEEN:
                return True
            SEEN.add(CUR)
            CUR = CUR.next
        return False