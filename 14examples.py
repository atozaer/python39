import random

# p78 ex2) 숫자 맞추기 (1~10)
# random.seed(221017)
# randomNum = random.randint(1,10)
#
# print('<<<숫자 맞추기 게임>>>')
# while True:
#     inputNum = int(input('숫자를 입력해주세요'))
#     if randomNum == inputNum:
#         print('정답입니다.')
#     else:
#         print('정답이 아닙니다.')


# ex30) 숫자 맞추기(1~100)
# random.seed(221017)
# randomNum = random.randint(1,100)
#
# while True:
#     inputNum = int(input('숫자를 입력해주세요!'))
#     if inputNum == randomNum:
#         print('정답입니다.')
#         break
#     elif randomNum < inputNum:
#         print('숫자가 커요!')
#     elif randomNum > inputNum:
#         print('숫자가 작아요!')
#     else:
#         print('올바른 숫자를 입력해주세요')


# ex25) 복권 프로그램
# 난수범위 - 100~999, 위치는 상관없이 숫자만 일치여부 판단
# ex) 123 -> 345(1), 317(2), 312(3)
# 문자열 슬라이싱을 위한 문자열 변환 str 함수 사용

# 3개 일치 - 상금 100만원!
# 2개 일치 - 상금 5만원!
# 1개 일치 - 상금 1천원!
# 0개 일치 - 다음 기회에!
lotto = []
randomNum = random.randint(1, 45)

for i in range(3):
    while randomNum in lotto:
        randomNum = random.randint(1,45)
    lotto.append(randomNum)

lotto.sort()
print(lotto)

match = 0
selectLotto = []
for i in range(3):
    selectLotto.append(int(input('로또 번호를 입력해주세요')))
selectLotto.sort()
print(selectLotto)

for i in range(len(lotto)):
    if lotto[i] == selectLotto[i]:
        match += 1

if match == 1:
    print("1개 당첨")
elif match ==2:
    print("2개 당첨")
elif match ==3:
    print("3개 당첨")
else:
    print('꽝')

