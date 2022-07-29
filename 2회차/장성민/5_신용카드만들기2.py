import sys

sys.stdin = open("_신용카드만들기2.txt")

T = int(input())

for tc in range(1, T + 1):
    li = list(input())
    
    for i in li:
        if i == '-':
            li.pop(li.index(i))
    
    cnt = 0
    for j in li:
        cnt += 1
    
    result = 0
    if (li[0] == '3' or li[0] == '4' or li[0] == '5' or li[0] =='6' or li[0] =='9') and cnt == 16:
        result = 1
    else:
        result = 0
        
    print(f'#{tc} {result}')
