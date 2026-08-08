class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for i in nums2:
            nums1.append(i)
        nums1.sort()
        a=len(nums1)//2
        if(len(nums1)%2!=0):
            return nums1[a]
        else:
            l=(nums1[a]+nums1[a-1])/2
            return l

        