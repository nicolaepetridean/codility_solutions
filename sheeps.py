def solution(X, Y):
    min_dist = max(max(X) + max(Y), 10)
    for i in range(len(X)-1):
        for j in range(i+1, len(X)):
            dist_x = abs(X[i] - X[j])
            dist_y = abs(Y[i] - Y[j])
            dist = max(dist_x, dist_y)
            if dist < min_dist:
                min_dist = dist
    return  min_dist // 2

if __name__ == '__main__' :
    print(solution([0, 0, 10, 10], [0, 10, 0, 10]))
    print(solution([1, 1, 8], [1, 6, 0]))
