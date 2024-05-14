TEST_CASE = int(input())
for t in range(TEST_CASE):
    N = int(input())
    print(f'#{t+1}')
    num = 1
    row = 0
    col = 0
    lst = []
    for i in range(N):
        lst.append([0]*N)

    for i in range(N):
        row = i
        for j in range(col,N-i):
            lst[row][j] = num
            num+=1
        col = j
        for j in range(row+1, N-i):
            lst[j][col] = num
            num+=1
        row = j
        for j in range(col-1, i, -1):
            lst[row][j] = num
            num+=1
        col = i
        for j in range(row, i+1, -1):
            lst[j][col] = num
            num+=1
    for row in lst:
        col_str = " ".join(map(str, row))
        print(col_str)
