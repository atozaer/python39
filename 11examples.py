



# ex) 윤년 여부를 출력하는 프로그램을 작성하세요
# 단, 3항 연산자를 이용해서 구현함

curYear = 2022
inputYear = int(input('연도를 입력해주세요'))

print(f'{inputYear:d}년은 윤년입니다.') \
    if (inputYear%4==0 and inputYear%100!=0) or inputYear%400==0 \
    else \
    print(f'{inputYear:d}년은 윤년이아닙니다.')

# ex) 년도와 월을 입력받아 윤년여부와 입력한 달의 마지막날을 출력하는 프로그램을 작성하세요
