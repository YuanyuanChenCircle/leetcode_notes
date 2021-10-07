# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# 1 2 3 4
# 2->1 3->2

class Solution:
    def reverseList(self, head):


        pre = None

        while head:

            temp = head.next

            head.next = pre

            pre = head

            head = temp

        return pre








