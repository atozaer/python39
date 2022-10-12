# 프로그래밍 언어 실습시 글꼴은 고정폭 글꼴을 사용할 것을 추천
# 1. 다음 내용을 출력하도록 프로그램을 작성해보세요
# print("*   *     **     ****     ****    *   *     ///////  ")
# print("*   *    *  *    *   *    *   *   *   *    | o   o |  ")
# print("*****   *    *   ****     ****     * *    (|   ∧   |) ")
# print("*   *   ******   *   *    *   *     *      |  [_]  |  ")
# print("*   *   *    *   *    *   *    *    *       _______   ")

# print("            +---+")
# print("            |   |")
# print("        +---+---+")
# print("        |   |   |")
# print("    +---+---+---+    /\_/\       ______     ")
# print("    |   |   |   |   ( ' ' )    / Hello  \   ")
# print("+---+---+---+---+   (  -  )   <  Junior  |  ")
# print("|   |   |   |   |    | | |     \ Coder! /   ")
# print("+---+---+---+---+   (__|__)      ------     ")

# 2. 다음의 출력화면을 구성하는 영수증 출력 프로그램을 작성하시오
# - 음식점에서 술과 안주를 먹고 금액을 계산하면 영수증을 받음
# - 영수증에는 메뉴항목과 단가, 수량, 가격, 총합계, 받은 금액, 10%의 부가세와 잔돈 등이 출력됨

# restaurant = "음식나라"
# soju = [('소주',3000)]
# chicken = [('치킨', 12000)]
#
# print('---------메뉴---------')
# print('1.소주')
# print('2.너나치킨')
#
# choice = input("주문할 메뉴를 선택하세요")
#
#
# print("[ "+ restaurant + " ]")
# print("---------------------")

# 3. 다음 중 자바 변수로 사용 가능한 것은 무엇인지 서술하여라.
# rate1, 1stPlayer, myprogram.java, long, TimeLimit, numberOfWindows
# rata1 = 1
# 1stPlayer = 2         # 변수명 숫자 X
# myprogram.java = 3    # . 때문에 불가
# long = 4
# TimeLimit = 5
# numberOfWindows = 6

# 4. 다음 수학식을 파이썬 표현식으로 바꿔보아라.
# x, y, z = 1, 2, 3
# s0, v0, t, g = 4, 5, 6, 9.8
# print(3 * x, 3 * x + y, (x + y) / 7)
# print(s0 + v0 * t + (1 / 2) * g * t ** 2)

# 5. 다음 문장의 실행결과는 무엇인지 서술하여라.
# 가. double number = ( 1 / 3 ) * 3;
# => 1.0
# number = (1/3)*3
# print(number)

# 나. quotient = 7 / 3;
# => 2.3333333333333335
# quotient = 7 / 3
# print(quotient)
#
# 다. int remainder = 7 % 3;
# => 1
# remainder = 7%3
# print(remainder)
#
# 라. int result = 11; ;
# => 5.5
# result = 11
# result /= 2
# print(result)

# 6. 다음 변수에 정의된 값을 이용해서 자바 표현식의 실행결과는
# 무엇인지 서술하여라.
# x = 2.5;  y = 1.5;  m = 18;  n = 4;

# 가.  x + n * y - (x + n) * y
# => -1.25
# print(x + n * y - (x + n) * y)

# 나.  m / n + m % n
# => 6.5
# print(m / n + m % n)

# 다.  5 * x - n / 5
# => 11.7
# print(5 * x - n / 5)

# 라.  1 - (1 - (1 - (1 - (1 - n))))
# => -3
# print(1 - (1 - (1 - (1 - (1 - n)))))

# 7. 각 표현식에 대한 결과 값을 계산하여라. 만일 틀린 식이 있다면 수정하여라.
#
# 가.  3 + 4.5 * 2 + 27 / 8
# 나.  true || false && 3 < 4 || !(5 == 7)
# print(True or False and 3 < 4 or not (5 == 7))
# 다.  true || (3 < 5 && 6 >= 2)
# print(True or 3 < 5 and 6 >= 2)
# 라.  !true > 'A'
# print(not True > bool('A'))     # not (True > True)
# 마.  7 % 4 + 3 - 2 / 6 * 'Z'
# print(7 % 4 + 3 - 2 / 6 * bool('Z'))
# 바.  'D' + 1 + 'M' % 2 / 3
# print(ord('D') + 1 + ord('M') % 2 / 3)
# 사.  5.0 / 3 + 3 / 3
# 아.  53 % 21 < 45 / 18
# 자.  (4 < 6) || true && false || false && (2 > 3)
# 차.  7 - (3 + 8 * 6 + 3) - (2 + 5 * 2)


# 12. 생년월일을 이용해서 나이를 계산하는 프로그램을 작성하여라. (MyAge)
# K나이 - 세는나이(출생시 1살, 해가 바뀌면 + 1)
#        만나이(출생시 0살, 생일이 지나면 + 1)
#        연나이(현재연도 - 출생연도)

# curDate = 2022
# birthDate = 1993
# isPassBirth = True
# myAge = curDate - birthDate
#
# print('연나이',myAge)
# print('세는나이', 1 + myAge)
#
# 파이썬 if 단축식 : 참일때 값 if 조건식, 거짓일 때 else 조건식
# print('만나이', (myAge+1) if isPassBirth else myAge)

# 13. 구구단 중 7단을 출력하는 프로그램을 작성하여라. (GuGu7Dan)
# print('7 x 1 = ', (7 * 1))
# print('7 x 2 = ', (7 * 2))
# print('7 x 3 = ', (7 * 3))
# print('7 x 4 = ', (7 * 4))
# print('7 x 5 = ', (7 * 5))
# print('7 x 6 = ', (7 * 6))
# print('7 x 7 = ', (7 * 7))
# print('7 x 8 = ', (7 * 8))
# print('7 x 9 = ', (7 * 9))

dan = 7
# .format
print("""
{0:d} x 1 = {0:d}
{0:d} x 2 = {1:d}
{0:d} x 3 = {2:d}
{0:d} x 4 = {3:d}
{0:d} x 5 = {4:d}
{0:d} x 6 = {5:d}
{0:d} x 7 = {6:d}
{0:d} x 8 = {7:d}
{0:d} x 9 = {8:d}
""".format(dan*1,dan*2,dan*3,dan*4,dan*5,dan*6,dan*7,dan*8,dan*9))

# f-string
print(f"""
{dan:d} x 1 = {dan*1:d}
{dan:d} x 2 = {dan*2:d}
{dan:d} x 3 = {dan*3:d}
{dan:d} x 4 = {dan*4:d}
{dan:d} x 5 = {dan*5:d}
{dan:d} x 6 = {dan*6:d}
{dan:d} x 7 = {dan*7:d}
{dan:d} x 8 = {dan*8:d}
{dan:d} x 9 = {dan*9:d}
""")



# 14. 다음 조건을 만족하는 프로그램을 작성하여라 (TimeTime)
# 하루는 86400초이다. 입력값이 1234567890일 경우 며칠인지 계산하여라
# 한 시간은 3600초이다. 입력값이 98765일 경우 몇 시간인지 계산하여라
# 일 분은 60초이다. 입력값이 12345일 경우 몇 분인지 계산하여라.


