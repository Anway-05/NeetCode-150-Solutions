class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        left=[-1]*len(heights)
        right=[len(heights)]*len(heights)
        stack=[]
        for i,x in enumerate(heights):
            while stack and heights[stack[-1]]>=x:
                stack.pop()
            if stack:
                left[i]=stack[-1]
            stack.append(i)
        stack=[]
        for i in range(len(heights)-1,-1,-1):
            x=heights[i]
            while stack and heights[stack[-1]]>=x:
                stack.pop()
            if stack:
                right[i]=stack[-1]
            stack.append(i)
        max_area=0
        for i in range(len(heights)):
            max_area=max(max_area,(right[i]-left[i]-1)*heights[i])
        return max_area


