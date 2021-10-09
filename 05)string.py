#참고 : http://pythonstudy.xyz/python/article/9-%EB%AC%B8%EC%9E%90%EC%97%B4%EA%B3%BC-%EB%B0%94%EC%9D%B4%ED%8A%B8

i=0

s ="반갑습니다."
s2 = '안녕하세요.'
s3 = '''환영합니다
이것은 문자열
입니다.'''
print(s3)

i=1
p = "이것은 %d번째 테스트 입니다." % (i)
print(p)

i=2
t = "ABC"
print(type(t))
print(type(t[1]),t[1])

i=3
st = ','.join(['가','나','다'])
print(st)

i=4
st=st.split(',')
print(st)
st=''.join(st)
print(st)

i=5
