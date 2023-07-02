

from collections import Counter
n = int(input())
a = [input() for i in range(n)]

word_count =    Counter(a)
print(len(word_count))
print(*(word_count).values())
