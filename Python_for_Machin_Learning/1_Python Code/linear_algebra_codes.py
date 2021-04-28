
"""Vector Addition"""
u = [2,2]
v = [2,3]
z = [3,5]
alpha = 5
result = [alpha * sum(t) for t in zip(u,v,z)]
print(result)




a = [[3,6],[4,5]]
b = [[5,7],[6,7]]

"""Matrix Addition"""
result1 = [[sum(i) for i in zip(*t)] for t in zip(a,b)]
print(result1)

"""Matrix Multiplication"""
result2 = [[sum(i * j for i, j in zip(row_a, column_b))for column_b in zip(*b)]for row_a in a]
print('result2', result2)



"""Scalar-Matrix Product"""
c = [[3,6],[4,5]]
d = 4
result3 = [[d * i for i in t] for t in c]
print(result3)


"""Matrix Transpose"""
e = [[1,2,3],[4,5,6]]
result4 = [[i for i in t] for t in zip(*e)]
print('result4', result4)

