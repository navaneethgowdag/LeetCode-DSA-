class Solution(object):
    def setZeroes(self, matrix):
        seen_row = set()
        seen_col = set()
        m,n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    seen_row.add(i)
                    seen_col.add(j)


        for i in range(m):
            for j in range(n):
                if i in seen_row or j in seen_col:
                    matrix[i][j] = 0

        return matrix