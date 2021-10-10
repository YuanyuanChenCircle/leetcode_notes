

class Solution:
    def getLeastNumbers(self, arr, k):

        # 快排

        start = 0
        end = len(arr) - 1

        self.quicksort(arr, start, end, k)

        return arr[:k]



    def quicksort(self, arr, start, end, k):

        if start >= end:

            return 

        pivotindex = self.partition(arr, start, end)

        if pivotindex > k - 1:
            self.quicksort(arr, start, pivotindex - 1, k)
        
        elif pivotindex < k - 1:

            self.quicksort(arr, pivotindex + 1, end, k)

        else:
            return




    def partition(self, arr, start, end):

        pivot = arr[start]

        left = start

        right = end

        index = start

        while right >= left:

            while right >= left:

                if arr[right] < pivot:

                    arr[left] = arr[right]
                    index = right
                    left += 1
                    break

                right -= 1


            while right >= left:

                if arr[left] > pivot:

                    arr[right] = arr[left]
                    index = left
                    right -= 1
                    break
                left += 1


            arr[index] = pivot

        return index



