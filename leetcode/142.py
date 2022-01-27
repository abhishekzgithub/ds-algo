"""
https://leetcode.com/problems/linked-list-cycle-ii/

Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously
following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer
is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

Do not modify the linked list.


Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def _detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow=fast=head

        while fast and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True
        return False
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow=fast=head
        while fast and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                break
        while head!=slow:
            head=head.next
            slow=slow.next
        return head.val

l2=[3,2,0,-4]
pos=1
l4=head=ListNode(l2[0])

head=A=ListNode(l2[0])
B=ListNode(l2[1])
C=ListNode(l2[2])
D=ListNode(l2[3])
A.next=B
B.next=C
C.next=D
D.next=B
# for i in range(1,len(l2)):
#     t2=ListNode(l2[i])
#     head.next=t2
#     head=head.next
# head.next=ListNode(l2[1])
# head=l4
print(Solution().detectCycle(head))