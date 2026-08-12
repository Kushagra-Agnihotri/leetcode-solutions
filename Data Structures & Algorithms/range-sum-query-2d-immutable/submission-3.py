class NumMatrix:
    def __init__(self, matrix):
        self.newMat = []
        for row in matrix:
            print(list(accumulate(row)))
            self.newMat.append(list(accumulate(row)))
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = 0
        for i in range(row1, row2+1):
            ans += self.newMat[i][col2]
            if col1 >= 1:
                ans-=self.newMat[i][col1-1]
        return ans

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)