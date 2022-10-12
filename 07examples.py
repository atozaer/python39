# ex) 주민번호에서 생년과 월, 일, 성별을 추출해서 각 변수에 적절히 저장하세요

# jumin = '930901-1234567'
# year = jumin[:2]
# month = jumin[2:4]
# day = jumin[4:6]
# gender = jumin[7:8]
#
# print(year)
# print(month)
# print(day)
# print(gender)


# 14. 다음 조건을 만족하는 프로그램을 작성하여라 (TimeTime)
# 하루는 86400초이다. 입력값이 1234567890일 경우 며칠인지 계산하여라
# 한 시간은 3600초이다. 입력값이 98765일 경우 몇 시간인지 계산하여라
# 일 분은 60초이다. 입력값이 12345일 경우 몇 분인지 계산하여라.

# sec = int(input("계산할 초를 입력하세요 : "))
# day = sec / 86400
# hour = sec / 3600
# minute = sec / 60
#
# print(f"""
# {day:.1f}일
# {hour:.1f}시간
# {minute:.1f}분
# """
# )

# 16. 고객에게 돌려줘야 하는 잔돈을 화폐단위로 계산하는 프로그램을 작성하시오.
# 즉, 잔돈을 돌려주기 위해 10원, 50원, 100원, 500원, 1000원, 5000원, 10000원, 50000원
# 등이 몇 개 필요한지 계산하는 것이다. (Charge)
#
# cost = 1234560
# money = 50000
# charge = money - cost
#
# w50000 = int(charge // 50000)
# charge = charge - (w50000 * 50000)
#
# w10000 = int(charge // 10000)
# charge = charge - (w10000 * 10000)
#
# w5000 = int(charge // 5000)
# charge = charge - (w5000 * 5000)
#
# w1000 = int(charge // 1000)
# charge = charge - (w1000 * 1000)
#
# w500 = int(charge // 500)
# charge = charge - (w500 * 500)
#
# w100 = int(charge // 100)
# charge = charge - (w100 * 100)
#
# w50 = int(charge // 50)
# charge = charge - (w50 * 50)
#
# w10 = int(charge // 10)
# charge = charge - (w10 * 10)
#
# print(f"""
#     지불 금액은 {cost:d}원 이고,
#     받은 금액은 {money}원 이고,
#     잔액은 {charge}원 입니다.
#
#     50,000원권은 {w50000}장, 10,000원권은 {w5000}장
#     5,000원권은 {w5000}장, 1,000원권은 {w1000}장
#     500원권은 {w500}개, 100원권은 {w100}개
#     50원권은 {w50}개, 10원권은 {w10}개
# """)

# cost = int(input('판매금액은 ? '))
# money = int(input('지불금액은 ?'))
# charge = money - cost
#
# w50000 = charge // 50000
# charge = charge % 50000
#
# w10000 = charge // 10000
# charge = charge % 10000
#
# w5000 = charge // 5000
# charge = charge % 5000
#
# w1000 = charge // 1000
# charge = charge % 1000
#
# w500 = charge // 500
# charge = charge % 500
#
# w100 = charge // 100
# charge = charge % 100
#
# w50 = charge // 50
# charge = charge % 50
#
# w10 = charge // 10
# charge = charge % 10
#
# print(f'''
#     지불 금액은 {cost:d}원 이고,
#     받은 금액은 {money}원 이고,
#     잔액은 {charge}원 입니다.
#
#     50,000원권은 {w50000}장, 10,000원권은 {w5000}장
#     5,000원권은 {w5000}장, 1,000원권은 {w1000}장
#     500원권은 {w500}개, 100원권은 {w100}개
#     50원권은 {w50}개, 10원권은 {w10}개
# ''')

# price = int(input('판매가를 입력해주세요'))
# inMoney = int(input(f'''지불금액을 입력해 주세요'''))
# difference = inMoney - price
# balance = 0
# cash = 50000
# fiftyThou = int((difference - balance) / cash)
# balance += fiftyThou * cash
# cash = 10000
# tenThou = int((difference - balance) / cash)
# balance += tenThou * cash
# cash = 5000
# fiveThou = int((difference - balance) / cash)
# balance += fiveThou * cash
# cash = 1000
# oneThou = int((difference - balance) / cash)
# balance += oneThou * cash
# cash = 500
# fiveHund = int((difference - balance) / cash)
# balance += fiveHund * cash
# cash = 100
# oneHund = int((difference - balance) / cash)
# balance += oneHund * cash
# cash = 50
# fifty = int((difference - balance) / cash)
# balance += fifty * cash
# cash = 10
# ten = int((difference - balance) / cash)
# balance += ten * cash
# print(
#     f"""
#     지불 금액은 {price}원 이고,
#     받은 금액은 {inMoney}원 이고,
#     잔액은 {difference}원 입니다.
#
#     50,000원권은 {fiftyThou}장, 10,000원권은 {tenThou}장
#     5,000원권은 {fiveThou}장, 1,000원권은 {oneThou}장
#     500원권은 {fiveHund}개, 100원권은 {oneHund}개
#     50원권은 {fifty}개, 10원권은 {ten}개
# """
# )


price = int(input('판매가를 입력해주세요'))
inMoney = int(input(f'''지불금액을 입력해 주세요'''))
difference = inMoney - price
balance = 0

balance = 0
for cash in [50000, 10000, 5000, 1000, 500, 100, 50, 10] :
    charge = (difference - balance) // cash
    balance += charge * cash
    print(f"{cash}원권은 {charge}장")