class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a,b=nums1,nums2
        if len(a)>len(b):
            a,b=b,a
        total=len(a)+len(b)
        l,r=0,len(a)
        half=(total+1)//2
        while l<=r:
            m=(l+r)//2
            l1=a[m-1] if (m-1)>=0 else float('-inf')
            r1=a[m] if m<len(a) else float('inf')
            l2=b[half-m-1] if (half-m-1)>=0 else float('-inf')
            r2=b[half-m] if (half-m)<len(b) else float('inf')
            if l1<=r2 and l2<=r1:
                if total%2==0:
                    return (max(l1,l2)+min(r1,r2))/2.0
                else:
                    return max(l1,l2)
            if l1>r2:
                r=m-1
            elif l2>r1:
                l=m+1