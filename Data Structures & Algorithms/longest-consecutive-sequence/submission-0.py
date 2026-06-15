class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lookup=set(nums)
        maximum=0
        for x in lookup:
            length=1
            current=x
            if x-1 not in lookup:
                while (current+1) in lookup:
                    length+=1
                    current+=1
                if length>maximum:
                    maximum=length
        return maximum

