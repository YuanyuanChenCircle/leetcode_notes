class Solution:
    def getLeastNumbers(self, arr, length):

        ##下沉调整
        def adjustHeap(self, parent_index, length):
            temp = arr[parent_index]
            child_index = 2 * parent_index + 1


            #构建大根堆
            while child_index < length:

                ##如果有右孩子，且右孩子大于左孩子的值，则定位到右孩子
                if child_index + 1 < length and arr[child_index] < arr[child_index + 1]:
                    child_index += 1

                #构建大根堆
                #如果父节点大于任何一个孩子的值，直接跳出
                if arr[child_index] < temp:
                    break

                arr[parent_index] = arr[child_index]
                parent_index = child_index
                child_index = 2 * child_index + 1

            arr[parent_index] = temp


        # arr = [2,3,4,5,6,7,1]

        #构建堆
        for i in range(len(arr)//2 - 1, -1, -1):
            adjustHeap(self, i, len(arr))

        print(arr)



        #调整堆结构
        for j in range(len(arr) - 1, 0, -1):

            #交换
            temp1 = arr[0]
            arr[0] = arr[j]
            arr[j] = temp1

            adjustHeap(self, 0, j)


        print("#####")
        print(arr)

if __name__ == '__main__':

    arr = [2,3,4,5,6,7,1,9]
    so = Solution()
    so.getLeastNumbers(arr,len(arr))