# Last updated: 7/14/2026, 2:16:54 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k==0 or not head or not head.next:
            return head
        
        length=1
        tail=head

        while tail.next:
            length +=1
            tail=tail.next
        
        final_k=k%length
        tail.next=head

        breaking_index=length-final_k-1

        current=head
        for i in range (breaking_index):
            current=current.next
        
        new_node=current.next
        current.next=None

        return new_node