from collections import List 


class Solution:
    '''
    These are both valid solutions with average time complexity
    O(nlogn) but the quickSort times out on the LeetCode problem. 
    '''

    def merge(self, arr, s, m, e):
        '''
        Merge sorted subarrays helper. This step is O(n)
        '''
        L = arr[s: m+1]
        R = arr[m+1: e+1]
        i, j, k = s, 0, 0 
        while j < len(L) and k < len(R):
            if L[j] < R[k]:
                arr[i] = L[j]
                j += 1
            else:
                arr[i] = R[k]
                k += 1
            i += 1
        while j < len(L):
            arr[i] = L[j]
            j += 1
            i += 1
        while k < len(R):
            arr[i] = R[k]
            k+=1
            i += 1


    def mergeSort(self, arr, s, e):
        '''
        mergeSort recursively sorts subarrays and 
        merges them together in order (see above helper)
        '''
        if e - s + 1 <= 1:
            # base case for length 1 or empty array
            return arr

        mid = (s+e) // 2
        self.mergeSort(arr, s, mid)
        self.mergeSort(arr, mid+1, e)
        self.merge(arr, s, mid, e)
        return arr


    def quickSortIndex(self, arr, s, e):
        '''
        Gets the index at which the left and right are
        less than or equal to and greater than or equal to
        the mid pivot respectively. This step is O(n)
        '''
        pivot = arr[(s+e) // 2]
        i = s - 1
        j = e + 1
        while True:
            i += 1
            while arr[i] < pivot: 
                i += 1
            j -= 1
            while arr[j] > pivot:
                j -= 1
            if i >= j:
                return j 
            arr[i], arr[j] = arr[j], arr[i]


    def quickSort(self, arr, s, e):
        '''
        quickSort by ordering elements to left and right
        of a midpoint pivot, recursively on subarrays. 
        '''
        if e - s + 1 <= 1:
            return arr
        mid = self.quickSortIndex(arr, s, e)
        self.quickSort(arr, s, mid)
        self.quickSort(arr, mid+1, e)
        return arr


    def sortArray(self, nums: List[int]) -> List[int]:
        
        return self.mergeSort(nums, 0, len(nums) - 1)
