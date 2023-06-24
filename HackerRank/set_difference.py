https://www.hackerrank.com/challenges/py-set-difference-operation/problem?isFullScreen=true

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
e = map(int, input().split())
m = int(input())
f = map(int,input().split())

new_set = set(e) - set(f)
print(len(new_set))
