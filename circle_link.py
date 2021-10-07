class Solution:
    def hasCycle(self, head):

        if head == None or head.next == None:
            return False


        # 环形链表

        quick = head.next

        slow = head

        while True:

            if quick == None or quick.next == None:
                return False

            if quick == slow:

                return True


            quick = quick.next.next

            slow = slow.next

            


