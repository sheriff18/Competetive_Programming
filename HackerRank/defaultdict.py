
from collections import defaultdict

n, m = map(int, input().split())
A = defaultdict(list)
B = defaultdict(list)

for i in range(1,1+n):
    A[input()].append(i)
for j in range(1,1+m):
    B[input()].append(j)

for word in B:
    if word in A:
        print(*A[word])
    else:
        print(-1)
