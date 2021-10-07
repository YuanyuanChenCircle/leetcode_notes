# class Solution:
#     def getIntersectionNode(self, headA, headB):




#         PA = headA
#         PB = headB

#         if PA == None or PB == None:

#             return None


#         while PA != PB:

            
            

#             PA = PA.next
            

#             PB = PB.next

#             if PA == None and PB == None:
#                 return None


#             if PA == None:

#                 PA = headB
#             if PB == None:

#                 PB = headA

            

#         return PA



class Solution:
    def getIntersectionNode(self, headA, headB):

        PA = headA
        PB = headB

        while  PA != PB:
            
            PA = PA.next 
            if PA else headB
            PB = PB.next
            if PB else headA

        return PA