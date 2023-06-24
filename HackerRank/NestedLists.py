

if __name__ == '__main__':
    students=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])
students.sort()
score_list=[]
for name, score in students:
    score_list.append(score)
score_set=list(set(score_list))
score_set.sort()
second_lowest_score=score_set[1]
for name, score in students:
    if score == second_lowest_score:
        print(name)
