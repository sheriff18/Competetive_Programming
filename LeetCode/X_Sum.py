

ef solve():
    n, m = map(int, input().split())
    chessboard = []
    for i in range(n):
        chessboard.append(list(map(int, input().split())))

    maximal = 0
    if n < 2 or m < 2:
        for row in chessboard:
            for element in row:
                maximal = max(element, maximal)
        print(maximal)
        return

    for i in range(n):
        for j in range(m):
            first_diagonal = 0
            y = i
            z = j
            while y > 0 and z > 0:
                y-=1
                z-=1
            while y < n and z < m:
                first_diagonal+=chessboard[y][z]
                y+=1
                z+=1
            
            second_diagonal = 0
            y = i
            z = j
            while y > 0 and z < m-1:
                y-=1
                z+=1
            while z >= 0 and y < n:
                second_diagonal+=chessboard[y][z]
                z-=1
                y+=1

            position_sum = first_diagonal + second_diagonal - chessboard[i][j]
            maximal = max(position_sum, maximal)
    print(maximal)

            

t = int(input())
for _ in range(t):
    solve()
