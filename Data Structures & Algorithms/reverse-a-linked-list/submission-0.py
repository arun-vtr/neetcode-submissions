# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        past=None
        present=head
        while present:
            future=present.next
            present.next=past
            past=present
            present=future
        return past
        