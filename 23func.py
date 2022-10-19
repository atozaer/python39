# 함수function
# 주어진 입력값으로 무언가를 수행하고 결과물을 내놓는 객체
# 한번 작성해두면 언제든 재사용 가능
# 논리적인 단위 분할 가능 -> 개발의 분업화
# 코드의 구현을 외부로 부터 숨길수 있음 -> 캡슐화

# 함수 정의
# def 함수이름(매개변수):
#     함수몸체

# 함수 호출
# 함수이름(인수)

# 인사말 출력하는 코드 1
# print('Hello, World!!')

# 인사말 출력하는 코드 2 - 3번 반복
# print('Hello, World!!')
# print('Hello, World!!')
# print('Hello, World!!')

# for _ in range(3):
#     print('Hello, World!!')

# 인사말 출력하는 코드 3
# 3번 반복하는 코드를 3번 반복한다면?
# 복붙으로 해결할 수 있지만, 유지보수가 쉽지않음
# for _ in range(3):
#     print('Hello, World!!')
# for _ in range(3):
#     print('Hello, World!!')
# for _ in range(3):
#     print('Hello, World!!')

# 인사말 출력하는 코드 4 - 함수
# def sayHello():
#     for _ in range(3):
#         print('Hello, World!!')
#
# sayHello()

# 매개변수(parameter) vs 인수(argument)
# 매개변수 : 함수 정의시 입력으로 전달된 값을 받는 변수
# 인수 : 함수 호출시 실제 입력으로 전달하는 값
# def sayHello(msg):
#     for _ in range(3):
#         print(f'Hello, {msg}!!')

# sayHello('Python')
# 'Python' : 함수 호출시 함수 내부로 전달하는 실제 값

# sayHello('Java')


# ex) 두 수를 입력 받아 add라는 함수로 호출해서 결과 출력
# 단, add라는 함수는 두 입력값을 더한 후 결과 출력함
# def addNums():
#     print(f'{a} + {b} = {a + b}')
#
# def addNums(a, b):
#     print(f'{a} + {b} = {a + b}')
#
# a = int(input('숫자를 입력해주세요'))
# b = int(input('숫자를 입력해주세요'))
#
# addNums(a, b)


# 함수 다중정의 - overloading
# 동일한 이름의 함수를 매개변수에 따라
# 다른 기능으로 동작하도록 작성하는 것을 의미
# 파이썬에서 공식적으로 지원하는 기능은 아님 - 구현가능
# 다중정의를 너무 남발하면 코드가 복잡해짐

# ex) 잔돈 계산하는 프로그램을 함수로 작성
# 함수명 : computeCharge(비용, 지불)

# def computeCharge(cost, money):
#     charge = money - cost
#
#     w50000 = charge // 50000
#     charge = charge % 50000
#
#     w10000 = charge // 10000
#     charge = charge % 10000
#
#     w5000 = charge // 5000
#     charge = charge % 5000
#
#     w1000 = charge // 1000
#     charge = charge % 1000
#
#     w500 = charge // 500
#     charge = charge % 500
#
#     w100 = charge // 100
#     charge = charge % 100
#
#     w50 = charge // 50
#     charge = charge % 50
#
#     w10 = charge // 10
#     charge = charge % 10
#
#     print(f'''
#     비용은 {cost:,d}원 이고,
#     받은 금액은 {money:,d}원 이고,
#     잔액은 {money-cost:,d}원 입니다.
#     50,000원권은 {w50000}장, 10,000원권은 {w10000}장
#     5,000원권은 {w5000}장, 1,000원권은 {w1000}장
#     500원권은 {w500}개, 100원권은 {w100}개
#     50원권은 {w50}개, 10원권은 {w10}개
#     ''')
#
# computeCharge(123450, 2345680)

# 더 간단한 버젼 #################
# def computeCharge(price, inMoney):
#     difference = inMoney - price
#     balance = 0
#
#     print(
#         f"""
#     지불 금액은 {price}원 이고,
#     받은 금액은 {inMoney}원 이고,
#     잔액은 {difference}원 입니다.
#     """)
#
#     for cash in [50000, 10000, 5000, 1000, 500, 100, 50, 10]:
#         charge = (difference - balance) // cash
#         balance += charge * cash
#         print(f"{cash}원권은 {charge}장")
#
# computeCharge(17500, 100000)


# ex) 신용카드 판별하는 프로그램을 함수로 작성
# 함수명 : checkCredit(코드)
# dict 자료구조를 이용해서 작성

# 33 - 신용카드 판별하는 프로그램을 함수로 작성
# 함수명 checkCredit(코드)
# dict 자료구조를 이용해서 작성
# card_info = {
#     35: {
#         'name': 'JCB카드',
#         'company_info': {
#             '6317': 'NH농협카드',
#             '6901': '신한카드',
#             '6912': 'KB국민카드',
#         },
#     },
#     4: {
#         'name': '비자카드',
#         'company_info': {
#             '04825': '비씨카드',
#             '38676': '신한카드',
#             '57973': '국민은행',
#         },
#     },
#     5: {
#         'name': '마스타카드',
#         'company_info': {
#             '15594': '신한카드',
#             '24353': '외환카드',
#             '40926': '국민은행',
#         },
#     },
# }
#
#
# def checkCredit(code):
#     if card_info.get(int(code[:2])):
#         print(card_info[int(code[:2])]['name'])
#         if card_info[int(code[:2])]['company_info'].get(code[2:]):
#             print(card_info[int(code[:2])]['company_info'][code[2:]])
#         else:
#             print('존재하지 않는 카드사 입니다.')
#     elif card_info.get(int(code[0])):
#         print(card_info[int(code[0])]['name'])
#         if card_info[int(code[0])]['company_info'].get(code[1:]):
#             print(card_info[int(code[0])]['company_info'][code[1:]])
#         else:
#             print('존재하지 않는 카드사 입니다.')
#     else:
#         print('존재하지 않는 카드 종류 입니다.')
#
#
# checkCredit('404825')


# ex) 60갑자를 출력해주는 프로그램을 함수로 작성
# 함수명 : checkChinaZodiac(년도)

def checkChinaZodiac(year):
    ganji = ('경', '신', '임', '계', '갑', '을', '병', '정', '무', '기')
    sip2ji = ('신', '유', '술', '해', '자', '축', '인', '묘', '진', '사', '오', '미')

    curgan = year % 10
    cursip = year % 12
    print(f'{ganji[curgan]}{sip2ji[cursip]}년 입니다.')

year = int(input('연도를 입력하세요 : '))
checkChinaZodiac(year)
