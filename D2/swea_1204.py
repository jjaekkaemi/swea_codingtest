TEST_CASE = int(input())
for t in range(TEST_CASE):
    tc = int(input())
    lst = list(map(int, input().split()))
    dic = {}
    for l in lst:
        if l not in dic:
            dic[l] = 0
        dic[l]+=1
        answer = l
    for d in dic:
        if dic[d]>dic[answer]:
            answer = d
    print(f'#{tc} {answer}')