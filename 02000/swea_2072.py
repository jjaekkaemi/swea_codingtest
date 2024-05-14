TEST_CASE = int(input())
for i in range(TEST_CASE):
    sum = 0
    lst = list(map(int, input().split()))
    for l in lst:
        if l%2 != 0 :
            sum += l
    print(f'#{i+1} {sum}')