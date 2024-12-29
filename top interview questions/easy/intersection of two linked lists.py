# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        current_A = headA
        current_B = headB
        while current_A != current_B:
            current_A = current_A.next if current_A else headB
            current_B = current_B.next if current_B else headA

        return current_A