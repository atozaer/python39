# 다중 if 문
# if~else만으로 다양한 조건을 판단하기 어려움
# => 물론 여러개의 if 문을 사용해서 처리 가능하기도 함
# 다양한 조건에 따라 판단하기 위해서는
# if ~ elif ~ else 구문을 사용해야 함

# if 조건식1:
#    조건식1이 참일때 실행할 문장
# elif 조건식2:
#    조건식2이 참일때 실행할 문장
# ...
# else:
#    거짓일때 실행할 문장

# 결과 조건 : 점수 0 ~ 50 => 노력하세요
#           51 ~ 80    => 잘했어요
#           81 ~ 100   => 최고예요
jumsu = 55

# if jumsu <= 50:
#     print('노력하세요')
# if jumsu <= 80:
#     print('잘했어요')
# if jumsu <= 100:
#     print('최고예요')
# => 결과가 올바르지 않게 나옴

if 0 <= jumsu <= 50:
    print('노력하세요')
if 51 <= jumsu <= 80:
    print('잘했어요')
if 81 <= jumsu <= 100:
    print('최고예요')

if jumsu <= 50:
    print('노력하세요')
else:
    if jumsu <= 80:
        print('잘했어요')
    else:
        if jumsu <= 100:
            print('최고예요')
# 들여쓰기를 조건에 따라 작성해야 함 - 가독성 저하

if jumsu <= 50:
    print('노력하세요')
elif jumsu <= 80:
    print('잘했어요')
elif jumsu <= 100:
    print('최고예요')
# 조건문장 작성시 들여쓰기를 일정하게 사용 - 가독성 상승

# 성적처리 프로그램 v3
# 이름, 국어, 영어, 수학을 입력받아
# 총점, 평균, 학점을 계산하고 출력함
# 학점처리 조건은 수우미양가로 함
name = input('이름이 뭐니?')
kor = int(input('국어 몇?'))
eng = int(input('영어 몇?'))
mat = int(input('수학 몇?'))

total = kor + eng + mat
avg = total / 3
# print(name, avg)

if avg <= 50:
    print(f'이름 : {name}, 평균 : {avg:.2f}, 학점 : 가')
elif avg <= 60:
    print(f'이름 : {name}, 평균 : {avg:.2f}, 학점 : 양')
elif avg <= 70:
    print(f'이름 : {name}, 평균 : {avg:.2f}, 학점 : 미')
elif avg <= 80:
    print(f'이름 : {name}, 평균 : {avg:.2f}, 학점 : 우')
elif avg <= 90:
    print(f'이름 : {name}, 평균 : {avg:.2f}, 학점 : 수')

name = input('이름을 입력해주세요\n')
kor, eng, mat = int(input('국어 : ?\n')), int(input('영어 : ?\n')), int(input('수학 : ?\n'))
tot = kor + eng + mat
avg = tot / 3
int_avg = int(avg)
unit = ''
if int_avg >= 90: unit = '수'
elif int_avg >= 80: unit = '우'
elif int_avg >= 70: unit = '미'
elif int_avg >= 60: unit = '양'
else: unit = '가'

print(f"""
이름 : {name}
국어 : {kor}, 영어 : {eng}, 수학 : {mat}
총점 : {tot}, 평균 : {int(avg)}({avg:.2f})
학점 : {unit}
""")

# ex) p.77 항공사 짐 무게 측정
cargo = int(input('짐의 무게는?(단위:kg)'))
result = '수수료가 없습니다'
# fee = cargo >= 10

if cargo >= 10:
    result = '수수료는 1만원입니다'

print(f'짐의 무게는 {cargo}kg 이고, {result}')

# ex) p.77 항공사 짐 무게에 따른 수수료 계산
cargo = int(input('짐의 무게는?(단위:kg)'))
result = '수수료가 없습니다'
pay = 0

if cargo >= 10:
    pay = (cargo // 10) * 10000
    result = f'수수료는 {pay}입니다'

print(f'짐의 무게는 {cargo}kg 이고, {result}')

# 연도를 입력받아 나이 계산한 후 나이에 따른 학생 분류 후 결과 출력
# 8 ~ : 초등학생
# 14 ~ : 중학생
# 17 ~ : 고등학생
# 20 ~ : 대학생
# 26 ~ : 학생이 아닙니다

oldyear = int(input('몇년생이니?'))
year = 2022
int_age = year - (oldyear - 1)

# if int_age < 8:
#     unit = '미취학'
# elif int_age < 14:
#     unit = '초등학생 입니다.'
# elif int_age < 17:
#     unit = '중학생 입니다.'
# elif int_age < 20:
#     unit = '고등학생 입니다.'
# elif int_age < 26:
#     unit = '대학생 입니다.'
# else:
#     unit = '학생이 아닙니다.'

if int_age >= 26:
    unit = '학생이 아닙니다.'
elif int_age >= 20:
    unit = '대학생 입니다.'
elif int_age >= 17:
    unit = '고등학생 입니다.'
elif int_age >= 14:
    unit = '중학생 입니다.'
elif int_age >= 8:
    unit = '초등학생 입니다.'
else:
    unit = '미취학'


print(f'''
출생년도 : {oldyear}
현재 나이는 {int_age}이고, {unit}
''')
