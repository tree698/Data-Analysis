result1 = []
for i in range(10):
    result1.append(i)

result2 = [i for i in range(10)]
result3 = [i for i in range(10) if i % 2 == 0]

word_1 = "Hello"
word_2 = "World"
result4 = [i+j for i in word_1 for j in word_2]

case_1 = ["A", "B", "C"]
case_2 = ["D", "E", "F"]
result5 = [i+j for i in case_1 for j in case_2]
result6 = [i+j for i in case_1 for j in case_2 if not(i == j)]
result7 = [i+j for i in case_1 for j in case_2 if i != j]

"""2차원 구조"""
result8 = [[i+j for i in case_1] for j in case_2]

"""sort 함수 주의"""
#result9 = result5.sort()
result5.sort()

words = "The quick brown fox jumps over the lazy dog".split()
stuff = [[w.upper(), w.lower(), len(w)] for w in words]
result10 = [i for i in stuff]

print("result1: ", result1)
print("result2: ", result2)
print("result3: ", result3)
print("result4: ", result4)
print("result5: ", result5)
print("result6: ", result6)
print("result7: ", result7)
print("result8: ", result8)
print("result5: ", result5)
# print("result9: ", result9)
print("result10: ", result10)


