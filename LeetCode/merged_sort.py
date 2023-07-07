

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = 0
        while i < m+n:
            if nums1[i] == 0:
                if len(nums2) != 0:
                    nums1.remove(nums1[i])
                    nums1.insert(i,nums2[0])
                    nums2.pop(0)
            i+=1
        nums1.sort()
