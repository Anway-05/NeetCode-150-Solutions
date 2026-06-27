class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        right=[len(heights)]*len(heights)
        left=[-1]*len(heights)
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
        print(left)
        print(right)
        max_area=0
        for i in range(len(heights)):
            print((right[i]-left[i]-1)*heights[i])
            if ((right[i]-left[i]-1)*heights[i])>max_area:
                max_area=((right[i]-left[i]-1)*heights[i])
        return max_area

