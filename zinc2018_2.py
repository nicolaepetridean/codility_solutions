# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

from itertools import product

def solution(A):
    if len(A) < 3:
        return 0

    a = [x for x in range(0, len(A) - 2)]
    b = [x for x in range(1, len(A) - 1)]
    c = [x for x in range(2, len(A))]

    possibilities = list(product(a,b,c))

    final_set = set()

    for (a,b,c) in possibilities:
        if a < b < c :
            final_set.add("".join((str(A[a]),str(A[b]),str(A[c]))))

    return len(final_set)



if __name__ == '__main__' :
    solution([2, 2, 1, 2, 2])