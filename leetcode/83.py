#https://leetcode.com/problems/remove-duplicates-from-sorted-list/
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr=head
        while curr and curr.next:
            if curr.val==curr.next.val:
                curr.next=curr.next.next
            else:
                curr=curr.next
        return head
#arr=[1,1,2]
arr=[1,1,2,3,3] #[1,2,3]
t=head=ListNode(arr[0])
for ele in range(1, len(arr)):
    t.next=ListNode(arr[ele])
    t=t.next

print(Solution().deleteDuplicates(head))