import sys

sys.stdin = open("_문자열의거울상.txt")

T = int(input())

for tc in range(1, T + 1):
    li = list(input())
    li.reverse()
    
    for i in range(len(li)):
        if li[i] == 'p':
            li[i] = 'q'
        elif li[i] == 'q':
            li[i] = 'p'
        elif li[i] == 'b':
            li[i] = 'd'
        elif li[i] == 'd':
            li[i] = 'b'
            
    result = ''.join(li)
    print(f'#{tc} {result}')