'''
num1 , num2
0(log(m+n))

nums1=[1,3]
nums2=[2]
median 2.0

nums1=[1,2]
nums2=[3,4]
median = 2+3/2 = 2.5

'''
class Solution:

    def find_median(self, nums1, nums2):
        m = len(nums1)
        n = len(nums2)
        if m < n:
            return self.find_median(nums1, nums2)

        # m = 5, n = 6 k=(5+6)-1=10
        k = (m+n)-1 # 10
        l=0
        r = min(m,k) # 5,10 r=5
        # start binary search
        # start the loop
        while l<r:
            # l = 0 , r = 5 , 2.5
            # 10-2.5 = 8.5
            midNums1 = (l+r)/2
            midNums2 = k-midNums1
