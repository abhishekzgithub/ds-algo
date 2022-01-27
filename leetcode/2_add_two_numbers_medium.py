"""https://leetcode.com/problems/add-two-numbers/

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, 
and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
"""

# Definition for singly-linked list.
from unittest import result


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def _addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry=0
        result=[]
        for ele1, ele2 in zip(l1,l2):
            print(ele1,ele2)
            temp=ele1+ele2+carry
            unit_place=temp%10
            tens_place=int(temp/10)
            result.append(unit_place)
            carry=tens_place
        return result
    
    def __addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry=0
        result=[]
        while l1!=None and l2!=None:
            temp=int(l1.val)+int(l2.val)+carry
            unit_place=temp%10
            tens_place=int(temp/10)
            result.append(unit_place)
            carry=tens_place
            l1=l1.next
            l2=l2.next
        l1=head=ListNode(result[0])
        i=1
        while i<len(result):
            t2=ListNode(result[i])
            head.next=t2
            head=head.next
            i+=1
        return l1

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry=0
        result=[]
        while l1!=None and l2!=None:
            temp=int(l1.val)+int(l2.val)+carry
            unit_place=temp%10
            tens_place=int(temp/10)
            result.append(unit_place)
            carry=tens_place
            l1=l1.next
            l2=l2.next
        while l1!=None:# or l2!=None:
            temp=int(l1.val)+carry
            unit_place=temp%10
            tens_place=int(temp/10)
            result.append(unit_place)
            carry=tens_place
            l1=l1.next
            
        while l2!=None:# or l2!=None:
            temp=int(l2.val)+carry
            unit_place=temp%10
            tens_place=int(temp/10)
            result.append(unit_place)
            carry=tens_place
            l2=l2.next
        if carry:
            result.append(carry)
        l1=head=ListNode(result[0])
        i=1
        while i<len(result):
            t2=ListNode(result[i])
            head.next=t2
            head=head.next
            i+=1
        return l1

#l1=[ListNode(2),ListNode(4),ListNode(3)]
#l2=[ListNode(5),ListNode(6),ListNode(4)]

l1=ListNode(2)
l1.next=ListNode(4)
l1.next.next=ListNode(3)


l2=ListNode(5)
l2.next=ListNode(6)
l2.next.next=ListNode(4)

l1=[9,9,9,9,9,9,9]
l2=[9,9,9,9]
expected=[8,9,9,9,0,0,0,1]
l3=head=ListNode(l1[0])
for i in range(1,len(l1)):
    t2=ListNode(l1[i])
    head.next=t2
    head=head.next

l4=head=ListNode(l2[0])
for i in range(1,len(l2)):
    t2=ListNode(l2[i])
    head.next=t2
    head=head.next

l1=l3
l2=l4
# l2=ListNode(5)
# l2=ListNode(5).next=ListNode(6).next=ListNode(4)
output=[7,0,8]
print(Solution().addTwoNumbers(l1,l2))