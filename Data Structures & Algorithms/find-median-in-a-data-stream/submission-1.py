class MedianFinder:

    def __init__(self):
        self.res = []
        
    def addNum(self, num: int) -> None:
        self.res.append(num)

    def merge_sort(self, arr):
        if len(arr) <= 1:
            return

        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        self.merge_sort(left)
        self.merge_sort(right)

        self.merge_sorted_list(left, right, arr)

    def merge_sorted_list(self, left, right, arr):
        len_l = len(left)
        len_r = len(right)

        i = j = k = 0

        while i < len_l and j < len_r:
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len_l:
            arr[k] = left[i]
            i += 1
            k += 1
        
        while j < len_r:
            arr[k] = right[j]
            j += 1
            k += 1

    def findMedian(self) -> float:
        if len(self.res) == 0:
            return None

        self.merge_sort(self.res)

        mid = len(self.res) // 2

        if len(self.res) % 2 == 0:
            return (self.res[mid] + self.res[mid - 1]) / 2
        else:
            return self.res[mid]