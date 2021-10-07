class CQueue:

    def __init__(self):

        self.stack = []
        self.stack1 = []

    def appendTail(self, value):
        self.stack.append(value)

    def deleteHead(self):

        if len(self.stack1) == 0:

           n = len(stack)

           while n != 0:
                
                self.stack1.append(self.stack.pop()) 

                n -= 1


        if len(self.stack1) == 0:
            return -1

        else:
            return self.stack1.pop()










# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()