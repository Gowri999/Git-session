def diagonal_difference(arr):
    primary_sum = 0
    secondary_sum = 0
    n = len(arr)

    for i in range(n):
        primary_sum += arr[i][i]   
        secondary_sum += arr[i][n - 1 - i] 

    return abs(primary_sum - secondary_sum)  


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

print(diagonal_difference(matrix)) 