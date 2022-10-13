# 반복문
# 정해진 회수만큼 특정코드를 실행하도록 만든 문장
# 파이썬에서는 for문과 while문이 지원

# 만일, 100번 출력해야 한다면 복붙을 계속할 것인가?
# 또한, 반복시 출력하는 문구가 변경된다면? - 다시 수정
# 효율적인 반복실행을 위해서 반복문을 사용함

# for 반복변수 in range(시작값, 종료값-1, 증감값):
#     반복실핼할 문장

# list(range(10))  # 0 ~ (10-1) 범위

# range(시작, 끝-1) = 시작값부터 끝값-1까지의 범위
# list(range(1, 45 + 1))

# range(시작, 끝-1, 증감값)
# => 시작값에서 증감값을 처리해서 끝값-1의 범위까지 출력
# list(range(2, 11, 2))

# ex) 1~100 사이 정수 출력
# print함수로 값 출력시 줄바꿈문자가 자동 추가됨
# 줄바꿈 문자 대신 다른 문자를 출력하려면 end 속성 사용
# for i in range(1,100+1):
#     print(i, end=' ')

# 100~1 사이 정수 출력
# for i in range(100,1,-1):
#     print(i, end=' ')

# for i in range(1, 100 + 1):
#     if i % 2 == 0: print(i, end=' ')

# 1 ~ 100 사이 정수 중 짝수만 출력
# for i in range(2,100+1,2):
#     print(i, end=' ')

# ex) 1 ~ 100 사이 정수들의 모든 합 계산후 출력
# hap = 0
# for i in range(1,100+1):
#     hap = hap + i
# print(hap)
#

# 가우스 덧셈공식을 이용해서 1~100 사이 모든 정수들의 합 계산 후 출력
# x~y까지의 숫자를 더한 합을 구하는 공식
# n = int(input())
# gaussSum = n * (n + 1) // 2
# print(gaussSum)

# for i in range(1,100+1):
#     hap += i + (101-i)
# hap = hap // 2
# print(hap)

# 문자열에 반복문 적용하기
# for i in 'Hello, World!!':
#     print(i, end=' ')

# ex) 단을 입력 받아 해당 단의 구구단을 출력
# dan = int(input('출력할 단을 선택해주세요 : '))
# for i in range(1, 9 + 1):
#     print(f'{dan} x {i} =  {dan * i}')

# p79 ex3) 3의 배수이지만 2의 배수는 아닌 정수 출력
# num = int(input('숫자를 입력하세요 : '))
# hap = 0
# result = ''
# for i in range(0, num):
#     if i % 3 == 0 and i % 2 != 0:
#         result += str(i) + ' '
#         hap += +i
# print(result)
# print('누적합 : ',hap)