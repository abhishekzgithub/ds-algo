"""
https://leetcode.com/problems/swapping-nodes-in-a-linked-list/
1721. Swapping Nodes in a Linked List

You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping the values 
of the kth node from the beginning and the kth node from the end (the list is 1-indexed).

Input: head = [1,2,3,4,5], k = 2
Output: [1,4,3,2,5]
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        temp=head
        slow=fast=head
        ll_length=self.find_length(temp)
        s=ll_length-k
        for i in range(s):
            fast=fast.next

        for j in range(0,k-1):
            slow=slow.next
        slow.val, fast.val=fast.val,slow.val
        return head

    def find_length(self, head1):
        temp=head1
        count=0
        while temp:
            count+=1
            temp=temp.next
        return count

l2=[7,9,6,6,7,8,3,0,9,5]

ll=[ListNode(i) for i in l2]
head_2=ll[0]
for inx in range(0,len(ll)-1):
    ll[inx].next=ll[inx+1]

k=5
sol=Solution()
sol.swapNodes(head_2,k)

        