class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merge = nums1 + nums2
        merge.sort()
        size = len(merge)
        if (size % 2) == 1:
            return float(merge[(size // 2)])
        else:
            return float((merge[size// 2] + merge[(size // 2) -1]) / 2)
        
