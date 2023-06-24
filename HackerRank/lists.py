https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true

if __name__ == '__main__':
    n = int(input())
    mylist = []
    
    for i in range(n):
        y = input().split()
        if y[0] == 'insert':
            mylist.insert(int(y[1]), int(y[2]))
        elif y[0] == 'print':
            print(mylist)
        elif y[0] == 'remove':
            mylist.remove(int(y[1]))
        elif y[0] == 'append':
            mylist.append(int(y[1]))
        elif y[0]== 'sort':
            mylist.sort()
        elif y[0] == 'pop':
            mylist.pop()
        else:
            mylist.reverse()
