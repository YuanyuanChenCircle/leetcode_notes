class Solution:
    def hasCycle(self, head):


        visited = set()

        while True:

            if head == None:
                return False

            if head in visited:

                return True

            visited.add(head)

            head = head.next


