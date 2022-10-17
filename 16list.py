# 파이썬 자료구조
# 자료구조는 대량의 데이터를
# 효율적으로 저장,조회,수정,삭제하기 위해
# 요구되는 기능과 기법을 의미
# 대표적인 자료구조 : 리스트, 튜플, 셋, 딕셔너리

# 리스트list
# 다른 프로그래밍 언어에서는 배열array과 유사
# 동일한(동일하지 않은) 형식의 데이터를
# 1차원 형태로 순차적으로 저장하는 자료구조 (중복허용)
# 선언방법은 값들을 []안에 정의하고 사용
# 리스트의 각 요소에 접근(참조)하려면 변수[인덱스] 형식을 사용

# menus = ['라면', '돈까스', '짜장면', '냉면', '정식']
# print(menus)

# 리스트에서 일부 요소(item,element)만 출력
# print(menus[0],menus[1],menus[2],menus[3],menus[4],)

# 리스트의 모든 요소 출력
# for i in range(len(menus)):
#     print(menus[i], end=' ')

# for menu in menus:      # 리스트의 요소를 하나씩 훑어가며 출력
#     print(menu, end=' ')

# 동적으로 리스트 생성하기
# menus = []  # 빈 리스트 선언

# 리스트에 요소를 추가하려면 append 함수
# append 한 요소는 리스트이 맨뒤에 부착 = FIFO
# menus.append('라면')
# menus.append('돈까스')
# menus.append('짜장면')
# menus.append('우동')
# menus.append('정식')

# 지정한 위치에 새로운 요소 추가 : insert(인덱스, 값)
# menus.insert(3, '냉면')

# 리스트요소의 값 수정 : 객체명[인덱스] = 새로운 값
# menus[3] = '탕수육'

# 리스트요소의 값 삭제 : remove(값) - 값으로 삭제
# menus.remove('탕수육')

# 리스트요소의 값 삭제 : pop(인덱스) - 위치로 삭제
# menus.pop(2)

# 리스트요소의 값 삭제 : pop() - 위치로 삭제, 뒤에서부터 하나씩 삭제
# menus.pop()

# 리스트로 다양한 데이터 다루기
# datas = []

# datas.append(1)
# datas.append(2.5)
# datas.append(True)
# datas.append('Hello')
# datas.append([1,3,5])
# print(datas)

# 성적프로그램 v2
# 이름,국어,영어,수학을 입력하면
# 총점,평균,학점을 처리해서 결과출력
# 단, 3명의 학생에 대해 성적처리를 진행함
# 성적자료 초기화



