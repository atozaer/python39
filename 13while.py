# while 반복문
# 횟수와는 상관없이 조건에 따라 반복실행하는 반복문
# 즉, 조건식의 결과가 참이면 실행하고, 거짓일 경우 실행을 중단함


# 변수초기화
# while 조건식:
#    반복실행할 문장
#    증감식

# ex) 1~100사이 정수 출력
# count = 1
# while count<=100:
#     print(count, end=' ')
#     count += 1

# ex) 1~100사이 정수 중 홀수만 출력
# count = 1
# while count<=100:
#     if count % 2 != 0:
#         print(count, end=' ')
#     count += 1

# ex) 단을 입력 받아 해당 단의 구구단을 출력
# i = 1
# dan = int(input('출력할 단을 선택해주세요 : '))
# while i<=9:
#     print(f'{dan} x {i} = {dan*i:2d}')
#     i += 1

# p79 ex3) 3의 배수이지만 2의 배수는 아닌 정수 출력
# i = 1
# result = ''
# hap = 0
# num = int(input('숫자를 입력해주세요 : '))
# while i<=num:
#     if i % 3 == 0 and i % 2 != 0:
#         result += str(i) + ' '
#         hap += +i
#     i += 1
# print(result)
# print('누적합:',hap)


# ex) 1~1000 사이의 모든 정수의 합을 출력하세요
# 단, 누적합이 15000이 넘으면 반복문을 중지하고 결과를 출력
# i = 1
# hap = 0
# while i<=1000:
#     if hap <= 15000:
#         hap = hap + i
#         i += 1
#     else:
#         print(hap)
#         print(i)
#         break


# 성적처리프로그램
# line = "-"*30
# while True:
#     print(f"""
#         성적처리프로그램
#         {line:s}
#           1. 성적 데이터 추가
#           2. 성적 데이터 조회
#           3. 성적 데이터 상세조회
#           4. 성적 데이터 수정
#           5. 성적 데이터 삭제
#           0. 프로그램 종료
#         {line:s}""")
#     selectMenu = input("작업을 선택하세요")
#     if selectMenu == '1':
#         print('성적데이터 추가')
#
#     elif selectMenu == '2':
#         print('성적 데이터 조회')
#
#     elif selectMenu == '3':
#         print('성적 데이터 상세조회')
#
#     elif selectMenu == '4':
#         print('성적 데이터 수정')
#
#     elif selectMenu == '5':
#         print('성적 데이터 삭제')
#
#     elif selectMenu == '0':
#         print('프로그램 종료')
#         break
#     else :
#         print('잘못된 번호를 입력하셨습니다.')


# ex) 1~1000 사이의 모든 정수의 합을 출력하세요
# 단, 누적합이 15000이 넘으면 반복문을 중지하고 결과를 출력
# i = 1
# hap = 0
# while i<=1000:
#     i += 1
#     if i % 7 == 0 or i % 9 == 0 :
#         continue
#     hap += i  # 상황에 따라 실행될수도, 실행되지 않을수도 있음
# print(hap)


# ex03) 아이디, 비밀번호를 입력받아
# 미리 설정해준 아이디, 비밀번호와 일치하면 '로그인성공!'
# 일치하지 않으면 '로그인 실패!'라고 출력하는 조건문 작성
# 아이디 : abc123 비밀번호 : 987xyz
# while True:
#     uid = input('아이디를 입력하세요')
#     pwd = input('비밀번호를 입력하세요')
#
#     if uid == 'abc123' and pwd == '987xyz' :
#         print('로그인 성공!')
#         break
#     else:
#         print('아이디와 비밀번호가 일치하지 않습니다.')
#         continue

# 난수 생성하기
# 파이썬에서 난수를 생성하려면 random 패키지 사용
# 생성방법 : 패키지명.random.randint(시작값, 끝값)
import random
random.seed(2210171044)

 # 난수생성 초기값 지정
# print(random.randint(1,10))

# 1~45 사이 임의의 정수 6개 생성
for _ in range(6):      # 반복 실행시 인덱스가 필요없으면 _ 사용
    print(random.randint(1, 45),end=' ')
