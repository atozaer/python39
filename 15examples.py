# ex48) 지금 현재 수지의 통장잔액이 25,000원이다.
# 은행이자가 연 6%라 가정할 때, 몇 년이 지나야 통장잔액이 지금의 2배를 넘는지 알아보는 프로그램을
# 아래 그림을 참고하여 작성하여라. (ComputeInvestment)

# money = 25000  # 통장잔액
# inter = 1.06  # 이율
# limit = money * 2

# while True:
#     if money > limit:
#         break
#     money = money * inter
#     count += 1

# for count in range(999):
#     if money > limit:
#         break
#     money = money * inter
#
# print(f"{count} 년째, 잔액은 {money:,.0f}원")


# ex51) 아래의 그림처럼 결과를 출력하는 프로그램을 작성하여라. (BigGugudan)


# ex53) 다음의 공식을 이용해서 입력한 년도의 1월 달력을 출력하는 프로그램을
# 작성하시오. (CalrendarV1)
# ( (년도-1)*365 + (년도-1)/4 - (년도-1)/100 + (년도-1)/400)  % 7) + 1 )
# 0 : 일, 1 : 월, 2 : 화, … … , 6 : 토

year = 2022

exyear31 = ((year - 1) * 365 + (year - 1) / 4 - (year - 1) / 100 + (year - 1) / 400) % 7

print(int(exyear31)) # 2021년 12월 31일의 요일
print(int(exyear31)+1) # 2022년 1월 1일의 요일
