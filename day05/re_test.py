import re

# a = 'hello, world!'
#  # print(re.match('world!',a))

#  # print(re.search('^world!',a))

# # print(re.search('world!$',a))


# str1 = '123 hello 678 HELLO'
# print(re.match('[0-9]+',str1))
# print(re.match('[0-9]*',str1))
#  # match : 무조건 앞에서부터 검색
# print(re.search('[0-9]*',str1))
#  # search : 상관 없음
#  # * : 0개 이상 / + : 1개 이상 / / : 0 또는 1개 이상 

# print(re.match('a*b','aaab'))
# print(re.match('a+b','ab'))

# print(re.search('^[0-9]{2,3}-[0-9]{4}-[0-9]{4}$','02-1111-1111 tel'))
#  # [이 범위 안에서]{필수숫자자리 수, 최대숫자자리 수}

#  # [^A] : A제외한~ / ^[A] : A로 시작하는 
#  # 문자로 특수문자 사용하고 싶으면 \하고 특수문자 EX) \*


# p = re.compile('^[a-z][a-z0-9_]{4,}@[a-z]{3,}[.][a-z]{2,}$')
# print(p.search('ss7up@gmail.com'))
# print(p.search('gpwls2014@gmail.com'))

p = re.compile('^[a-z][a-z0-9_]{4,}@[a-z]{3,}[.][a-z]{2,}$')
email = ''
while not p.search(email):
# └ none 값이 나오면 나올때까지 계속하도록
    email = input('email >>> ')
    
