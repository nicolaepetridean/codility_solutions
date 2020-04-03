def solution(A):
    if len(A) == 0:
        return 0

    def search_around(A, row, column, code):
        # stopping conditions
        if row < 0 or row >= len(A) or column < 0 or column >= len(A[row]):
            return
        if A[row][column] != code:
            return
        # mark the teritory as belonging to the same country
        A[row][column] = -1
        # search down
        search_around(A, row + 1, column, code)
        # search right
        search_around(A, row, column + 1, code)
        # search up
        search_around(A, row - 1, column, code)
        # search left
        search_around(A, row, column - 1, code)

    countries = 0
    for i in range(len(A)):
        for j in range(len(A[i])):
            if A[i][j] != -1:
                code = A[i][j]
                search_around(A, i, j, code)
                countries += 1

    return countries


if __name__ == '__main__' :
    solution([[5,4,4], [4,3,4], [3,2,4], [2,2,2], [3,3,4], [1,4,4], [4,1,1]])