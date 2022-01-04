class NQueens:
    def __init__(self, col=4, row=4):
        
        pass
        
    # def __str__(self):
    #     return str(self.matrix)

    def is_horizontal_match(self, matrix, i, j):
        for col in range(len(matrix)):
            if matrix[i][col]=="Queen":
                return True
        return False

    def is_vertical_match(self, matrix, i, j):
        for row in range(len(matrix)):
            if matrix[row][j]=="Queen":
                return True
        return False

    def is_diagonal_match(self, matrix, i, j):
        r,q=i,j
        while r>=0 and q>=0:
            if matrix[r][q]=="Queen":
                return True
            r-=1
            q-=1
        rr,rc=i,j
        while rr>=0 and rc<len(matrix):
            if matrix[rr][rc]=="Queen":
                return True
            rr-=1
            rc+=1
        return False
    
    def is_valid(self,matrix, i, j):
        if not (self.is_vertical_match(matrix, i, j) 
                or self.is_horizontal_match(matrix, i, j)
                or self.is_diagonal_match(matrix, i, j)
                ):
            return True
        return False

    def set_queen(self, matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if self.is_valid(matrix, i, j):
                    matrix[i][j]="Queen"
        return matrix
    
    def printSolution(self,mat):
        for r in mat:
            print(str(r).replace(',', ' ').replace('\'', ''))
        print()

    def set_nqueen(self, matrix, r):
        if r==len(matrix):
            self.printSolution(matrix)
            return
        for j in range(len(matrix[0])):
            if self.is_valid(matrix, r, j):
                matrix[r][j]="Queen"
                self.set_nqueen(matrix, r+1)
                matrix[r][j]="0"
        return None

    def get_matrix(self, r_size, c_size):
        x = []
        y = []
        for j in range(0, c_size):
            y.append("0")
        for i in range(0, r_size):
            x.append(y[:])
        return x

obj=NQueens()
matrix=obj.get_matrix(4,4)
print(obj.set_nqueen(matrix,0))