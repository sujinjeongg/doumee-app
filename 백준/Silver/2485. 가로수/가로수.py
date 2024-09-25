import math

N = int(input())

trees = [int(input()) for _ in range(N)]

#등차 구하기
gaps = [] 
for i in range(1, N):
    gaps.append(trees[i]-trees[i-1])
gcd_gap = gaps[0] #공차 = 원소 간 차이들의 최대공약수
for gap in gaps:
    gcd_gap = math.gcd(gcd_gap, gap)

#새로 심어야 할 가로수 개수 구하기
count = 0
for gap in gaps:
    count += (gap // gcd_gap) - 1

print(count)