def subarray_sum(number, array):
    start = 0
    end = 1

    while start < len(array) and end < (len(array) + 1):
        total = sum(array[start:end])
        if total < number:
            end += 1
            total = sum(array[start:end])
        if total > number:
            start += 1
            total = sum(array[start:end])
        elif total == number:
            start += 1
            return (str(start) + ' ' + str(end))
        print(total)

    return ('-1')

case=1
N=[5,12]
A=[1,2,3,7,5]
cases = int(input())

for case in range(cases):
    N = list(map(int, input().split()))
    N = N[1]
    A = list(map(int, input().split()))
    print(subarray_sum(N, A))
    print(subarray_sum(N, A))

