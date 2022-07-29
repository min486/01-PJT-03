import sys

sys.stdin = open("_신용카드만들기1.txt")

T = int(input())

for tc in range(1, T + 1):
    li = list(map(int, input().split()))
    
    one_list = []
    for i in li[0:16:2]:
        one_list.append(i * 2)
    one = sum(one_list)
    
    two_list = []
    for j in li[1:16:2]:
        two_list.append(j)
    two = sum(two_list)
    
    # 아래 내용 fail?
    for N in range(10):
        if ((one + two + N) // 10) == 0:
            print(f'#{tc} {N}')