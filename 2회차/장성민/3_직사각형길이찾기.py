import sys

sys.stdin = open("_직사각형길이찾기.txt")

T = int(input())

for tc in range(1, T + 1):
    li = list(map(int, input().split()))
    li.sort()
    result = li[0] + li[2] - li[1]

    print(f'#{tc} {result}')