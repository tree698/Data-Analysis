"""splite() String type을 List 형태로 변환"""

items1 = 'zero one two three'.split()    # 빈칸을 기준으로 분리 --> 리스트 형태로 출력

items2 = 'python, jquery, javascript'
items3 = items2.split(",")               #
a, b, c = items2.split(",")              # 쉼표 기준으로 분리하여 a,b,c 변수에 대입

items4 = 'cs50.gachon.edu'
subdomain, domain, tld = items4.split(".")

print('items1:', items1)
print('items3:', items3)
print('a:', a)
print(type(a))
print('b:', b)
print('c:', c)
print('a,b,c:', a, b,c)
print("subdomain:", subdomain)
print("domain:", domain)
print("tld:", tld)
print("subdomain, domain, tld:", subdomain, domain, tld)


"""String List를 합쳐 하나의 String으로 반환"""

colors = ['red', 'blue', 'green']
result1 = ''.join(colors)
result2 = ' '.join(colors)  # 공백
result3 = ','.join(colors)  # 쉼표
result4 = '-'.join(colors)  # 하이픈

print('result1:', result1)
print('result2:', result2)
print('result3:', result3)
print('result4:', result4)


