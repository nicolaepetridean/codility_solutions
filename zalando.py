# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

from array import array


def solution(A):
    (n, m) = (len(A), len(A[0]))

    row = 0
    column = 0

    result = [str(A[0][0])]

    max = []

    while (row < n - 1):
        max = 0
        right = False


    while (row < n-1 or column < m-1):
        max = 0
        right = False
        if row+1 <= n-1:
            if max < A[row+1][column]:
                max = A[row+1][column]
        if column+1 <= m-1:
            if max < A[row][column+1]:
                right = True

        if right:
            result.append(str(A[row][column+1]))
            column += 1
        else:
            result.append(str(A[row+1][column]))
            row += 1

    return "".join(result)


if __name__ == '__main__' :
    #solution([[9,9,7], [9,7,2], [6,9,5], [9,1,2]])
    #solution([[9],[9],[9],[9],[1],[2],[3]])
    solution([[2,2,2,2],[2,2,2,7],[2,2,2,2],[2,2,2,2]])