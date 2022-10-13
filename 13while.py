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
i = 1
hap = 0
while i<=1000:
    if hap <= 15000:
        hap = hap + i
        i += 1
    else:
        print(hap)
        print(i)
        break
