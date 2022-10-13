# 20. if 문을 실행하고 난 뒤의 변수의 값을 서술하여라
# 가. int n = 1; int k = 2; int r = n;     if ( k < n ) r = k;
# 나. int n = 1; int k = 2; int r;         if ( n < k ) r = k; else r = k + n;
# 다. int n = 1; int k = 2; int r = k;     if ( r < k ) n = r; else k = n;
# 라. int n = 1; int k = 2; int r = 3;     if ( r < n + k ) r = 2 * n; else k = 2 * r;
import random

# 22. number 변수에 30과 35가 입력된다고 가정할 때
# 각각의 if문의 결과는 무엇인가요?
# 1.
# if ( number % 2 == 0 )
# System.out.println( number + " is even." );
# System.out.println( number + " is odd." );
# 2.
# if ( number % 2 == 0 )
#   System.out.println( number + " is even." );
# else
# System.out.println( number + " is odd." );


# 25. 다음 조건을 만족하는 복권 발행 프로그램을 작성하세요. (Lotto)
# 가. 사용자로부터 복권 숫자 3자리를 입력 받으세요 (yourkey)
# 나. 변수에 임의의 복권 숫자 3자리를 초기화합니다 (lottokey)
# 다. 사용자가 입력한 복권 숫자가 모두 일치 : 상금 1백만 지급
# 라. 일치하지 않는 경우 : “아쉽지만, 다음 기회를!” 라고 출력

# lotto = [3,6,9]
# yourkey = []
# yourkey.append(int(input('복권숫자1 : ')))
# yourkey.append(int(input('복권숫자2 : ')))
# yourkey.append(int(input('복권숫자3 : ')))
#
# if sorted(lotto) == sorted(yourkey):
#     print('당첨')
# else:
#     print('탈락')

# 26. 사용자가 연봉과 결혼 여부를 입력하면 다음의 세금율에 의해 납부해야
# 할 세금을 계산하는 프로그램을 작성하세요 (Tax)
# 가. 미혼인 경우 : 연봉 3000미만 - 10%,  연봉 3000이상 - 25%
# 나. 결혼한 경우 : 연봉 6000미만 - 15%,  연봉 6000이상 - 35%

salary = int(input('연봉을 입력하세요 : '))
isMarreid = False
merriedCheck = input('결혼 여부를 입력해주세요 y/n')
if merriedCheck == 'y':
    isMarreid = True

if isMarreid:
    if salary < 6000:
        print(f'세율 : 15%, 납부액:{int(salary*0.15):d}원')
    elif salary >= 6000:
        print(f'세율 : 35%, 납부액:{int(salary*0.35):d}원')
else:
    if salary < 3000:
        print(f'세율 : 10%, 납부액:{int(salary*0.1):d}원')
    elif salary >= 3000:
        print(f'세율 : 25%, 납부액:{int(salary*0.25):d}원')

# 27. 다음 조건을 이용해서 현재 연도를 입력하면 윤년 여부를
# 출력하는 프로그램을 작성하세요. (LeapYear)
# 가. 현재 연도가 4로 나눠 떨어지지만, 100으로는 나눠 떨어지지 않음
# 나. 현재 연도가 400으로 나눠 떨어짐

# curYear = int(input('현재 연도를 입력하세요 : '))
# if (curYear % 4 == 0 and curYear % 100 != 0) or curYear % 400 == 0:
#     print('윤년입니다.')
# else:
#     print('윤년이 아닙니다.')