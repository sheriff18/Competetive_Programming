https://www.hackerrank.com/challenges/zipped/problem?isFullScreen=true

# Enter your code here. Read input from STDIN. Print output to STDOUT
N,X = map(int, input().split())

l = []

for i in range(X):
    a = list(map(float,input().split()))
    l.append(a)

new = list(zip(*l))

for i in new:
    print(sum(i)/X)
    
