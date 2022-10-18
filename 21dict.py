# dict
# 비순차 자료구조
# 키를 통해 값을 찾는 연관배열 객체
# 선언방법은 { 키:값 } 형태로 정의하고 사용
# 다양한 자료형으로 구성된 데이터를
# 하나의 변수로 접근할 수 있음

# dict 선언
member = {'userid': 'abc123', 'passwd': '987xyz'}

# dict 값 조회 : 객체명['키명']
# print(member['userid'], member['passwd'])

# dict 모든 키 조회 : 객체명.keys()
# print(member.keys())

# for key in member.keys():
#     print(key, end=' ')
# print()

# dict 모든 값 조회 : 객체명.values()
# print(member.values())

# for value in member.values():
#     print(value, end=' ')
# print()

# dict 모든 키/값 조회 1 : 객체명.items()
# print(member.items())

# for k,v in member.items():
#     print(f'({k},{v})', end=' ')

# dict 모든 키/값 조회 2 : 키 이용(추천!)
# for k in member.keys():
#     print(member[k], end=' ')

# dict 모든 키/값 조회 3 : 객체명.get(키) 이용(추천!)
# for k in member.keys():
#     print(member.get(k), end=' ')


# dict 동적 생성 1
# user = {}       # 사용자 - 이름, 나이, 이메일로 구성
#
# user['name'] = '홍길동'
# user['age'] = 22
# user['email'] = 'gildong@hong.com'
#
# print(user)

# dict 동적 생성 2 : dict(키=값,...)
# user2 = dict(name='홍길동', age = 44, email = 'honggil@dong.com')
# print(user2)

# dict 동적 생성 3 : list 이용 - [키 [키, 값],...]
# user3 = [
#     ['name', '홍길동'],
#     ['age', 66],
#     ['email', 'hong@gil.com']
# ]
# print(dict(user3))

# dict 수정하기 : 객체명[기존키] = 새로운값
#
# user['name'] = '홍길순'
# user['age'] = 77
# user['email'] = 'gildong111@hong.com'
# print(user)

# dict 삭제하기 : del 객체명[기존키] - 키와값 모두삭제
# del user['age']
# print(user)

# 객체명.get(키) vs 객체명[키]
# user['regdate']     #존재하지 않는 키 호출시 - 오류표기
# 오류 발생시 예외처리 코드로 적절히 대처

# user.get('regdate')     # 존재하지 않는 키 호출시 - 오류표기X
# 반환값이 None 인지


# ex1) dict 자료구조를 이용해서 학생 1명분의 데이터를 처리
# 저장형식 : { name :??, kor :??, eng :??, mat :??, tot :??, avg :??, grd :??,}

# line = "-" * 30
# main_menu = f"""
#     성적처리프로그램 v2b
#     {line:s}
#       1. 성적 데이터 추가
#       2. 성적 데이터 조회
#       3. 성적 데이터 상세조회
#       4. 성적 데이터 수정
#       5. 성적 데이터 삭제
#       0. 프로그램 종료
#     {line:s}"""
# while True:
#     print(main_menu)
#     selectMenu = input("메뉴를 선택하세요 => ")
#
#     if selectMenu == '1':
#         student = {}
#         student['name'] = input('이름은?')
#         student['kor'] = int(input('국어 점수는?'))
#         student['eng'] = int(input('영어 점수는?'))
#         student['mat'] = int(input('수학 점수는?'))
#         student['tot'] = student['kor'] + student['eng'] + student['mat']
#         student['avg'] = student['tot'] / 3
#         student['grd'] = '가'
#
#         if student['avg'] >= 90 :
#             student['grd'] = '수'
#         elif student['avg'] >= 80:
#             student['grd'] = '우'
#         elif student['avg'] >= 70:
#             student['grd'] = '미'
#         elif student['avg'] >= 60:
#             student['grd'] = '양'
#
#     for k,v in student.items():
#         print(f'{k}:{v}',end=' ')
#
#     print(student)

# ex2) dict 자료구조를 이용해서 학생 3명분의 데이터를 처리
# 저장형식 : { name :??, kor :??, eng :??, mat :??, tot :??, avg :??, grd :??,}

students = []
student = {}

for i in range(3):
    student['name'] = input('이름은?')
    student['kor'] = int(input('국어 점수는?'))
    student['eng'] = int(input('영어 점수는?'))
    student['mat'] = int(input('수학 점수는?'))
    student['tot'] = student['kor'] + student['eng'] + student['mat']
    student['avg'] = student['tot'] / 3
    student['grd'] = '가'

    if student['avg'] >= 90:
        student['grd'] = '수'
    elif student['avg'] >= 80:
        student['grd'] = '우'
    elif student['avg'] >= 70:
        student['grd'] = '미'
    elif student['avg'] >= 60:
        student['grd'] = '양'

    students.append(student)

for student in students:
    print(student)

# dict 형식 데이터 출력시 예쁘게 표시 : pretty print
from pprint import pprint as pp

pp(student)