# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):

        head_l1 = l1
        head_l2 = l2

        # 遍历链表
        temp = []

        head = ListNode(0)
        cur = head

       
        move = 0
        while head_l1 != None and head_l2 != None:


            sum_data = head_l1.val + head_l2.val + move

            
            de = sum_data%10

            temp.append(de)

            head.next = ListNode(de)

            head = head.next
            
            move = sum_data//10


            head_l1 = head_l1.next
            head_l2 = head_l2.next

        if head_l1 == None:

            while head_l2:

                sum_data = head_l2.val + move

                de = sum_data%10


                temp.append(sum_data)
                head_l2 = head_l2.next
                head.next = ListNode(de)

                move = sum_data//10



                head = head.next
        else:

            while head_l1:

                sum_data = head_l1.val + move

                de = sum_data%10

                temp.append(de)

                head_l1 = head_l1.next

                head.next = ListNode(de)
                move = sum_data//10

                head = head.next

        if move >= 1:
            head.next = ListNode(move)
            head = head.next

        return cur.next








