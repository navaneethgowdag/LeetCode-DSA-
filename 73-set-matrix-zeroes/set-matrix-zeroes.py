class Solution(object):
    def setZeroes(self, matrix):
        ans = []
        m,n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    ans.append([i,j])
        i = 0
        while (i != len(ans)):
            zero = ans[i]
            row = zero[0]
            col = zero[1]
            for r in range(m):
                matrix[r][col] = 0
            
            for c in range(n):
                matrix[row][c] = 0
            i += 1

        return matrix