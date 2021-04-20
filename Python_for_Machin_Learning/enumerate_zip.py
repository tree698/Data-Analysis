"""enumerate: List 요소를 번호를 붙여 추출"""

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

mylist = ["a", "b", "c"]
result1 = list(enumerate(mylist))

result2 = {i:j for i, j in enumerate('Gachon Universit is an academic institute located in Seoul'.split())}

print('result1:', result1)
print('result2:', result2)


"""zip:  List의 각 index 값끼리 묶어 병렬적으로 추출"""

alist = ["a1", "a2", "a3"]
blist = ["b1", "b2", "b3"]
for i, j in zip(alist, blist):
    print(i, j)

a,b,c = zip((1,2,3), (10, 20, 30), (100, 200, 300))
sum_ = [sum(x) for x in zip((1, 2, 3), (10, 20, 30), (100, 200, 300))]

print('a,b,c:', a,b,c)
print('sum_:', sum_)


for i, (a,b) in enumerate(zip(alist, blist)):
    print(i, a, b)

