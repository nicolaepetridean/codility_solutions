# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    if len(A) < 3:
        return 0

    day_1_index = 0
    day_2_index = 1
    day_3_index = 2

    possibilities = set()
    n = len(A)

    while day_1_index <= n - 3:
        posibility = (str(A[day_1_index]), str(A[day_2_index]), str(A[day_3_index]))
        possibilities.add("".join(list(posibility)))

        if (day_3_index < n -1):
            day_3_index += 1
            continue
        if (day_2_index < n - 2):
            day_2_index += 1
            day_3_index = day_2_index + 1
            continue
        if (day_1_index < n - 3):
            day_1_index += 1
            day_2_index = day_1_index + 1
            day_3_index = day_2_index + 1
        else :
            break


    return len(possibilities)



if __name__ == '__main__' :
    solution([1, 2, 3, 4])