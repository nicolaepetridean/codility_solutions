
from itertools import combinations

def compute_efficiency(A,B, list_of_dev):
    sum = 0
    for i in list_of_dev:
        sum += A[i]
    for i in range(len(B)):
        if i not in list_of_dev:
            sum += B[i]

    return sum

def solution2(A, B, F):
    # write your code in Python 3.6
    # Get all combinations of A
    # and length 2
    list_of_dev = [x for x in range(len(A))]
    combs = combinations(list_of_dev, F)

    maxx = 0
    for combination in combs:
        eff = compute_efficiency(A, B, combination)
        if eff > maxx :
            maxx = eff

    return maxx

def solution(A, B, F):
    C=[] #There will be two dimmensioned array where is every element [productivity in A team, difference in productivity]
    team1=team2=0
    for x in range(0,len(A)): C.append([A[x]-B[x],A[x]]) #filling C
    C.sort(reverse=True)
    for x in range(0,F): team1 += C[x][1] #counting productiviy in team1
    for x in range(F,len(A)): team2 += C[x][1]-C[x][0] #counting productiviy in team2
    return (team1+team2)


if __name__ == '__main__' :
    # print(solution([5, 5, 5], [5, 5, 5], 1))
    print(solution([7, 1, 4, 4], [5, 3, 4, 3], 2))
    # print(solution([4, 2, 1], [2, 5, 3], 2))
    # print(solution([4], [20], 1))