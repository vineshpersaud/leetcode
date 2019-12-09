class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sum = nums1 + nums2
        sum.sort()
        half = len(sum) / 2.0
        if len(sum) % 2.0 != 0.0:
            return sum[math.floor(half)]
        else :
            return (sum[int(half-1)] + sum[int(half)])/2.0
