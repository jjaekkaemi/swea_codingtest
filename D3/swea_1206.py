TEST_CASE = 10
for i in range(TEST_CASE):
    N = int(input())
    buildings = list(map(int, input().split()))
    max_num = 0
    answer = 0
    for l in range(N):
        max_num = 0
        if l-2>-1 and l+3<=N:
            for j in range(l-2, l):
                max_num = max(max_num, buildings[j])
            for j in range(l+1, l+3):
                max_num = max(max_num, buildings[j])
            diff = buildings[l]-max_num
            answer += diff if diff>0 else 0
    print(f'#{i+1} {answer}')