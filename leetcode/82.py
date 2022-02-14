#https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head):
        
        sentinel=ListNode(0,head)
        prev=sentinel
        while head:
            if head.next and (head.val==head.next.val):
                while(head.next and (head.val==head.next.val)):
                    head=head.next
                prev.next=head.next
            else:
                prev=prev.next
            head=head.next
        return sentinel.next
#arr=[1,1,2]
arr=[1,1,2,3,3] #[1,2,3]
arr=[1,2,3,3,4,4,5]
arr=[1,1,1,2,3]

t=head=ListNode(arr[0])
for ele in range(1, len(arr)):
    t.next=ListNode(arr[ele])
    t=t.next

print(Solution().deleteDuplicates(head))