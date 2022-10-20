# 컨프리헨션comprehension
# 다양한 데이터 객체에 사용하는 복잡한 구문을
# 단순하게 작성할 수 있도록 지원

# 파이썬에는 4가지 축약을 지원
# list(py2), set(py3), dict(py3), generator(py3)

# 리스트에 적용하는 축약
# 1 ~ 10까지의 정수를 생성해서 리스트에 저장
a = list(range(1, 10 + 1))
print(a)

b = []
for i in range(1, 10 + 1):
    b.append(i)
print(b)

# 리스트 for 축약문
# [표현식 for 항목 in 반복가능개체]
c = [i for i in range(1, 10 + 1)]
print(c)

# ex) 1 ~ 20 사이 정수 중 짝수를 리스트로 생성
d1 = [i for i in range(1, 20 + 1) if i % 2 == 0]
d2 = [i * 2 for i in range(1, 10 + 1)]
d3 = [i for i in range(2, 20 + 1, 2)]
print(d1, "\n", d2, "\n", d3)

# ex) 1 ~ 10 사이 정수를 제곱한 값을 리스트로 생성
e = [i ** 2 for i in range(1, 10 + 1)]
print(e)

# ex) 아래 각각의 리스트를 이용해서 제곱값을 계산하고
# 새로운 리스트에 생성하세요
val1 = [1, 2, 3, 4, 5]
val2 = [1, 2, 'A', False, 9, 100]

val1s = [i ** 2 for i in val1]
print(val1s)

val2s = [i ** 2 for i in val2]  # 오류발생
print(val2s)

# 조건식을 이용해서 재작성 - 정수일 경우 제곱 연산
# for if 축약문
# [표현식 for 항목 in 반복가능개체 if 조건]
val2s = [i ** 2 for i in val2 if type(i) == int or type(i) == bool]
print(val2s)

# ex) 1~60 사이 정수 중 홀수만 골라 리스트에 저장
f1 = [i for i in range(1, 60 + 1, 2)]
f2 = [i for i in range(1, 60 + 1) if i % 2 == 1]
print(f1, "\n", f2)

# ex) 1~60 사이 정수 중 5의 배수만 골라 리스트에 저장
g1 = [i for i in range(5, 60 + 1, 5)]
g2 = [i for i in range(1, 60 + 1) if i % 5 == 0]
print(g1, "\n", g2)

# ex) 1~100 사이 정수 중 임의의 정수가 짝수면 'even'
# 홀수면 'odd'라고 구분해서 리스트에 저장
h1 = [['even', 'odd'][i % 2] for i in range(1, 100 + 1)]
print(h1)

# for 다중 if 축약문 : 3항연산자 적용
# [표현식1 if 조건 else 표현식2 for 항복 in 반복가능개체]
h2 = ['even' if i % 2 == 0 else 'odd' for i in range(1, 100 + 1)]
print(h2)

# ex) 구구단 중 7,8단의 결과값을 리스트에 저장
# [7, 14, 21, .... , 8, 16, 24, ..., 72]
# 중첩 for 축약
# [표현식 for 항목1 in 반복가능개체1 for 항목2 in 반복가능개체2]
gu = [i * j for i in range(7, 8 + 1) for j in range(1, 9 + 1)]  # 앞:상위for, 뒤:하위for
print(gu)

gugu = [f'{i} * {j} = {i * j}' for i in range(7, 8 + 1) for j in range(1, 9 + 1)]
print(gugu)

# ex) name, grd 리스트의 값들을
# 각각의 키와 값으로 딕셔너리에 저장
name = ['혜교', '지현', '수지']
grd = ['우', '미', '수']

# 단순하게 작성
# 새로운 dict요소 생성 : 객체명[키이름] = 값
s = {}
for idx, v in enumerate(grd):
    s[name[idx]] = v
print(s)

# 딕셔너리 for 축약문
# {키값표현식 for key, value 항목 in zip(반복가능개체1, 반복가능개체2)}
s2 = {k: v for k, v in zip(name, grd)}
print(s2)

# ex) 학생과 국어점수에 대한 리스트가 있을때
# 학생은 키로, 합격여부를 값으로 하는 딕셔너리 객체를 생성
# 단, 합격여부에는 국어점수가 85점이상인 경우 '합격'
# 그외는 '불합격'이라고 출력함
name = ['철수', '영희', '길동', '꺽정']
kor = [50, 80, 90, 60]

# 딕셔너리 for if 축약문
# {키 : 표현식1 if 조건식 else 표현식2 for key, value 항목 in zip(반복가능개체1, 반복가능개체2)}
r = {k: '합격' if v >= 85 else '불합격' for k, v in zip(name, kor)}
print(r)

# p111 ex3)
message = ['spam', 'ham', 'spam', 'ham', 'spam']

# A) spam은 1로 ham은 0으로 생성하는 dummy 변수 생성
dummy = [1 if v == 'spam' else 0 for v in message]
print(dummy)

# map 사용
dummy2 = list(map(lambda v: 1 if v == 'spam' else 0, message))
print(dummy2)

# B) sapm 원소만 추출
spam = [v for v in message if v == 'spam']
print(spam)

# filter 사용
spam2 = list(filter(lambda v: True if v == 'spam' else False, message))
print(spam2)

spam3 = list(filter(lambda v: v == 'spam', message))
print(spam3)
