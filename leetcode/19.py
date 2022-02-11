"""
https://leetcode.com/problems/remove-nth-node-from-end-of-list/
Given the head of a linked list, remove the nth node from the end of the list and return its head.
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
"""
import copy
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)

class Solution(object):

    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        n=n-1
        temp=copy.deepcopy(head)
        curr=prev=head
        ll_length=self.find_length(temp)
        if n+1==ll_length:
            return head.next
        index=1
        pos=ll_length-n
        while curr:
            if index==pos:
                break
            prev=curr
            curr=curr.next
            index+=1
        prev.next=curr.next
        return head

    def find_length(self, head1):
        temp=head1
        count=0
        while temp:
            count+=1
            temp=temp.next
        return count

    def find_node(self, original_head, pos, count):
        node=None
        temp=original_head
        while temp:
            count-=1
            if count==pos:
                node=temp
                node.next=None
            temp=temp.next
        return node

l2=[1,2]#,3,4,5]
l2=[4,5,4]
head_1=A=ListNode(l2[0])
B=ListNode(l2[1])
C=ListNode(l2[2])
# D=ListNode(l2[3])
# E=ListNode(l2[4])
A.next=B
B.next=C
# C.next=D
# D.next=E

n=1
sol=Solution()
#s=sol.find_length(head_1)
#print(sol.find_node(head_1,n,s))
print(sol.removeNthFromEnd(head_1, n))
        