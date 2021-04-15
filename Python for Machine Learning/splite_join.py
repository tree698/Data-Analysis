"""String Type을 분리하여 List 형태로 변환"""

item = 'zero one two'.split()
print(item)

example = 'python, jquery, javascript'.split(',')
print(example)

example = 'python, jquery, javascript'
a, b,c = example.split(',')
print(a)
print(b)
print(c)

example = 'cs50.gachon.edu'
subdomain, domain, tld = example.split('.')
print(subdomain)


"""String LIst를 합쳐 하나의 String으로 반환"""

colors = ['red', 'blue', 'green', 'yellow']
result = ''.join(colors)
print(result)

result = ' '.join(colors)
print(result)

result = '-'.join(colors)
print(result)