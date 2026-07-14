# Last updated: 7/14/2026, 2:16:28 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast=head
        slow=head

        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        
        dummy=None
        temp=slow.next

        while slow:
            temp=slow.next
            slow.next=dummy
            dummy=slow
            slow=temp

        first=head
        second=dummy

        while first and second:
            if first.val !=second.val:
                return False
            
            first=first.next
            second=second.next
        
        return True