# 조건문
# 조건에 따라 프로그램의 실행 순서를 조정하는 문장

# ex1) 입력한 어떤 수가 짝수인지 판단하는 조건문

# num = int(input('숫자를 입력하세요'))
# if num % 2 == 0:
#     print('짝수입니다.')
# else:
#     print('홀수입니다.')
#
# if int(input('정수 하나를 입력 하세요')) % 2 :
#     print("홀 수 입니다.")
# else :
#     print("짝 수 입니다.")

# ex2) 점수를 3개 입력받아 평균이 60이상이고,
# 각 점수가 40점 이상이면 합격이라 출력하는 조건문 작성

# kor = int(input('점수1:'))
# eng = int(input('점수2:'))
# math = int(input('점수3:'))
# avg = (kor + eng + math) / 3
# if avg >= 60 and kor >= 40 and eng >= 40 and math >= 40:
#     print('합격입니다.')
# else:
#     print('불합격입니다.')

# score1, score2, score3 = int(input('점수1')), int(input('점수2')), int(input('점수3'))
# if min(score1, score2, score3) >= 40 and (score1 + score2 + score3) / 3 > 60:
#     print('합격')
# else:
#     print('불합격')


# ex03) 아이디, 비밀번호를 입력받아
# 미리 설정해준 아이디, 비밀번호와 일치하면 '로그인성공!'
# 일치하지 않으면 '로그인 실패!'라고 출력하는 조건문 작성
# 아이디 : abc123 비밀번호 : 987xyz

# uid = 'abc123'
# pwd = '987xyz'
#
# inputUid = input('아이디:')
# inputPwd = input('비밀번호:')
# if inputUid == uid and inputPwd == pwd:
#     print('로그인 성공')
# else:
#     print('로그인 실패')
    
