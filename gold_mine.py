
def solution(N, M, X, Y):
    if not check_numar_of_mines_is_even(len(X)):
        return 0

    result = 0
    count = 0
    nr_of_rows = len(X)
    desired_minex_on_x = nr_of_rows / 2

    nr_of_cols = len(Y)
    desired_minex_on_y = nr_of_cols / 2


    for i in range(N):
        if i in X:
            count += X.count(i)

        if count == desired_minex_on_x:
            result += 1

    count = 0
    for i in range(M):
        if i in Y:
            count += Y.count(i)
        if count * 2 == desired_minex_on_y:
            result += 1

    return result

def check_numar_of_mines_is_even(nr):
    return (nr % 2) == 0

if __name__ == '__main__' :
    # print(solution(5, 5, [0, 4, 2, 0], [0, 0, 1, 4]))
    # print(solution(5, 5, [0, 0, 0, 0], [0, 2, 1, 3]))
    # print(solution(5, 5, [2], [2]))
    # print(solution(5, 5, [0,4], [0,4]))
    # print(solution(5, 5, [], []))
    #
    # print(solution(5, 5, [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4],
    #                [0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4]))

    print(solution(6, 6, [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5],
                   [0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5]))