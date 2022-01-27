"""
https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/
2095. Delete the Middle Node of a Linked List

You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.

The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, 
where ⌊x⌋ denotes the largest integer less than or equal to x.

    For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.

Input: head = [1,3,4,7,1,2,6]
Output: [1,3,4,1,2,6]
Explanation:
The above figure represents the given linked list. The indices of the nodes are written below.
Since n = 7, node 3 with value 7 is the middle node, which is marked in red.
We return the new list after removing this node. 
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):

    def split(self, head):
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        middle=slow.next
        slow.next=None
        first_half, second_half = head, middle
        return first_half, second_half

    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head.next==None:
            return []
        first_half, second_half = self.split(head)
        temp=first_half
        while temp.next.next:
            temp=temp.next
        temp.next=second_half
        return first_half


l2=[1,2,3,4,5]
head=A=ListNode(l2[0])
B=ListNode(l2[1])
C=ListNode(l2[2])
D=ListNode(l2[3])
E=ListNode(l2[4])
A.next=B
B.next=C
C.next=D
D.next=E

sol=Solution()
sol.deleteMiddle(E)