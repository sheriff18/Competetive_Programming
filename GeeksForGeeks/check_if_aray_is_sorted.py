https://practice.geeksforgeeks.org/problems/check-if-an-array-is-sorted0701/1
class Solution:
    def arraySortedOrNot(self, arr, n):
        i = 0
        j = i + 1
        
        while i < j and j < n:
            if arr[i] > arr[j]:
                return False
            i += 1
            j += 1
        
        return True
