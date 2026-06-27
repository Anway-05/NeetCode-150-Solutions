class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r=1,max(piles)
        while l<=r:
            time_taken=0
            m=((l+r)//2)
            for x in piles:
                time_taken+=((x+m-1)//m)
            if time_taken<=h:
                k=m
                r=m-1
            else:
                l=m+1
        print(l,k)
        return k
            
