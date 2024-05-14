TEST_CASE = int(input())
for i in range(TEST_CASE):
    N = int(input())
    lst = list(map(int, input().split()))
    max_num = 0
    answer = 0
    for l in reversed(lst):
        if max_num<l:
            max_num = l
        else:
            answer += max_num-l
    print(f'#{i+1} {answer}')