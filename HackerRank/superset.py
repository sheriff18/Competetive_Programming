https://www.hackerrank.com/challenges/py-check-strict-superset/problem?isFullScreen=true

# Enter your code here. Read input from STDIN. Print output to STDOUT
A = set(list(map(int, input().split())))
n = int(input())

for i in range(n):
    y = set(list(map(int, input().split())))
    if A.issuperset(y)== False:
        print('False')
        break
else:
    print('True')
