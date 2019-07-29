from collections import Counter
import bisect


# code
def find(X, Y, M, N):
    occ = Counter(Y)
    count = 0
    Y.sort()
    for x in X:
        if x == 0:
            continue
        if x == 1:
            count += occ.get(0, 0)
            continue
        p = bisect.bisect_right(Y, x)
        count += (N - p)

        count += (occ.get(0, 0) + occ.get(1, 0))

        if x == 2:
            count -= (occ.get(3, 0) + occ.get(4, 0))
        if x == 3:
            count += occ.get(2, 0)

    return count


T =1# int(input())

while T:
    [M, N] =[3,2]
    X = [2,1,6]#list(map(int, input().split()))
    Y = [1,5]#(map(int, input().split()))
    print(find(X, Y, M, N))
    T -= 1
