TEST_CASE = 10
for t in range(TEST_CASE):
    answer = 0
    dump_count = int(input())
    lst = list(map(int, input().split()))
    lst.sort()
    min_num = lst.pop(0)
    max_num = lst.pop(len(lst)-1)
    while dump_count :
        min_num+=1
        max_num-=1
        for i in range(len(lst)):
            if min_num<=lst[i]:
                lst.insert(i, min_num)
                break
        for i in range(len(lst)-1, -1, -1):
            if max_num>=lst[i]:
                lst.insert(i+1, max_num)
                break
        min_num = lst.pop(0)
        max_num = lst.pop(len(lst)-1)
        diff = max_num-min_num
        if diff <=0 :
            break
        dump_count-=1
    print(f'#{t+1} {diff}')