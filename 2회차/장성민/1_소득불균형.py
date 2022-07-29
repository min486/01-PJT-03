import sys

sys.stdin = open("_소득불균형.txt")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    li = list(map(int, input().split()))
    
    sum_ = 0
    for i in li:
        sum_ += i
    avg = sum_ // N
    
    avg_people =0
    for j in li:
        if j <= avg:
            avg_people += 1
            
    print(f'#{tc} {avg_people}')