"""https://leetcode.com/problems/reorder-list/
# reverse linked list

You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln

Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Input: head = [1,2,3,4]
Output: [1,4,2,3]

Hint: split into half
reverse the other half
merge both
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


    def reverse(self, head):
        prev=None
        curr=head
        while curr:
            temp=curr.next #save the next link
            curr.next=prev #reverse the link to backwards
            prev=curr #swap curr with prev
            curr=temp# move forward
        head=prev #move prev to head so that it acts at a beginning and not curr
        return prev
    
    def print_ll(self,head1):
        print("printing")
        while head1:
            print(head1.val)
            head1=head1.next

    def merge(self,head1,head2):
        temp1,temp2=head1,head2
        while temp2:
            temp=temp1.next
            temp1.next=temp2
            temp1=temp2
            temp2=temp
        return head1
    
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        first_half, second_half=self.split(head)
        head1=self.reverse(second_half)
        head=self.merge(first_half,head1)
        return head


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

head1=A1=ListNode(l2[0])
B1=ListNode(l2[1])
C1=ListNode(l2[2])
D1=ListNode(l2[3])
E1=ListNode(l2[4])
A1.next=B1
B1.next=C1
C1.next=D1
D1.next=E1
sol=Solution()
#head=(sol.reorderList(head))
#sol.print_ll(head)
# head1=sol._split(head)
# sol.print_ll(head1)
# first_half, second_half=sol.find_mid(head1)
# sol.print_ll(first_half)
# sol.print_ll(second_half)
# head1=sol.reverse(second_half)
# sol.print_ll(head1)
# head=sol.merge(first_half,head1)
# sol.print_ll(head)

head=sol.reorderList(head1)
sol.print_ll(head)