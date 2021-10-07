def partition(arr, start, end):

    pivot = arr[start]
    left = start
    right = end
    index = start
    # 坑的位置，初始等于pivot的位置
    while right >= left:
        # right指针从右向左进行比较
        while right >= left:

            if arr[right] < pivot:

                arr[left] = arr[right]
                index = right
                left += 1
                break
            right -= 1

        # left指针从左向右比较
        while right >= left:

            if arr[left] > pivot:

                arr[right] = arr[left]
                index = left
                right -= 1
                break

            left += 1

        arr[index] = pivot

    return index

def qiuck_sort(arr, start, end):

    if start >= end:

        return
    pivot_index = partition(arr, start, end)

    qiuck_sort(arr, start, pivot_index - 1)
    qiuck_sort(arr, pivot_index + 1, end)


if __name__ == '__main__':

    arr = [3,2,3,1,2,4,5,5,6,7,7,8,2,3,1,1,1,10,11,5,6,2,4,7,8,5,6]

    qiuck_sort(arr, 0, len(arr) - 1)

    print(arr)











