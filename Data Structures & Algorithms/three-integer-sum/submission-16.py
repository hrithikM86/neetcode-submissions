class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.merge_sort(nums)

        for i, a in enumerate(nums):
            l = i+1
            r = len(nums)-1

            while l < r:
                thresome = a + nums[l] + nums[r]
                lst = [a, nums[l], nums[r]]

                if (thresome == 0) and (lst not in res):
                    res.append(lst)
                    l+=1
                elif (thresome > 0):
                    r-=1
                else:
                    l+=1

        return res
                
                


                


    




    def merge_sort(self, arr):
            if len(arr) <= 1:
                return 

            mid = len(arr)//2

            left = arr[:mid]
            right = arr[mid:]

            self.merge_sort(left)
            self.merge_sort(right)
            
            self.merge_sorted_list(left, right, arr)

    def merge_sorted_list(self,a,b,arr):
        
            len_a = len(a)
            len_b = len(b)

            i = j = k = 0

            while i < len_a and j < len_b:
                if a[i] <= b[j]:
                    arr[k] = a[i]
                    i+=1
                else:
                    arr[k] = b[j]
                    j+=1
                k+=1
            
            while i < len_a:
                arr[k] = a[i]
                i+=1
                k+=1

            while j < len_b:
                arr[k] = b[j]
                j+=1
                k+=1

        
        