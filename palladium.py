# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(H):
    # find big jumps

    max_val = H[0]
    max_val_poz = 0
    second_max = H[0]
    second_max_poz = 0
    third_max = H[0]
    third_max_poz = 0

    max_jump_position = []
    max_jump = 0

    for i in range(1, len(H)):
        jump = H[i] - H[i-1]
        if jump > max_jump:
            max_jump = jump
            max_jump_position.append(i)
        if jump > max_jump:
            max_jump = jump
            max_jump_position.append(i)
        if H[i] > max_val:
            third_max = second_max
            third_max_poz = second_max_poz
            second_max = max_val
            second_max_poz = max_val_poz
            max_val = H[i]
            max_val_poz = i
            continue
        if H[i] > second_max:
            third_max = second_max
            third_max_poz = second_max_poz
            second_max = H[i]
            second_max_poz = i
            continue
        if H[i] > third_max:
            third_max = H[i]
            third_max_poz = i


    first_cost = max_val * len(H)

    if len(positions) == 1:
        condidate_sum =




if __name__ == '__main__' :
    solution([2,2,2,2])