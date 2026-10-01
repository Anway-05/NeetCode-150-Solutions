class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        up,down,left,right=0,len(matrix)-1,0,len(matrix[0])-1
        final=[]
        while up<=down and left<=right:
            for i in range(left,right+1):
                final.append(matrix[up][i])
            up+=1
            for i in range(up,down+1):
                final.append(matrix[i][right])
            right-=1
            if up<=down:
                for i in range(right,left-1,-1):
                    final.append(matrix[down][i])
                down-=1
            if left<=right:
                for i in range(down,up-1,-1):
                    final.append(matrix[i][left])
                left+=1
        return final

        