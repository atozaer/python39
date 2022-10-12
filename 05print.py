# print 함수

# 성적처리 프로그램 v1
# 이름, 국어, 영어, 수학을 이용해서
# 총점, 평균을 계산하고 출력함

# 출력 1
name = "홍길동"
kor = 99
eng = 98
math = 88
total = kor + eng + math
avg = total / 3
print("이름:",name,"총점:",total,"평균:",avg)

# 출력 2 - 출력서식 사용 : %사용
# print(출력서식 % 변수들)
print('이름: %s 총점: %04d 평균: %.2f' % (name, total, avg))

# 출력 3 - format() 함수 사용
print('이름:',format(name,'s'),'총점:',format(total,'d'),'평균:',format(avg,'.2f'))

# 출력 4 - 인덱스, 출력서식 사용 : .format 함수 사용
# print('{인덱스:출력서식}'.format(변수들...))
print('이름 : {0:s}'.format(name))
print('국어 : {:03d} 영어 : {:03d} 수학 : {:03d}'.format(kor,eng,math))   # 인덱스 생략가능
print('총점 : {0:d}, 평균 : {1:.2f} ({1:.1f})'.format(total,avg))        # 특정변수 반복출력 가능
print('총점 : {1:d}, 평균 : {0:.2f} ({0:.1f})'.format(avg,total))        # 순서상관없이 인덱스에 따라 출력가능

# 출력 5 - 문자열 템플릿(f-string) : python 3.6부터 지원 (추천)
# print(f'{변수명:출력서식}')   출력서식 생략가능
print(f'이름 : {name:s}')
print(f'국어 : {kor:d} 영어 : {eng:d} 수학 : {math:d}')
print(f'총점 : {total:d} 평균 : {avg:.1f}')

