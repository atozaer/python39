# 파일읽기 : 파일 내 데이터 읽어오기
# 파일객체변수 = open(경로, 모드)        # py2
# with open(경로, 모드) as 파일객체변수  # py3

# 파일모드 : 파일작업 종류
# r(읽기, 생략가능), t(텍스트파일 읽기), b(바이너리파일 읽기)

# 파일읽을때 사용가능 함수
# read    : 텍스트파일의 내용을 모두 읽음
# readline : 텍스트파일의 내용을 한줄씩 읽어옴 (반복문사용)
# readlines : 텍스트파일의 내용을 한줄씩 모두 읽어옴

# 간단한 인삿말을 파일에서 읽어오기
f = open('hello.dat')
doc = f.read() #파일 내용을 모두읽어 문자열로 저장
f.close()
print(doc)

with open('hello.dat') as f:
    doc2 = f.read()
print(doc2)

# 인삿말이 저장된 hello2.dat 파일에서도 읽어오기
with open('hello2.dat', encoding='UTF-8') as f:
    doc3 = f.read()
print(doc3)

# 여러건의 회원정보가 저장된 파일 읽어오기 1
with open('sungjuk.dat', encoding='UTF-8') as f:
    doc4 = f.read() # 모두 읽기
print(doc4)

# 여러건의 회원정보가 저장된 파일 읽어오기 2
with open('sungjuk.dat', encoding='UTF-8') as f:
    doc5 = f.readlines()
print(doc5)

# 여러건의 회원정보가 저장된 파일 읽어오기 3
with open('sungjuk.dat', encoding='UTF-8') as f:
    doc6 = f.readline() # 행 단위로 하나씩 읽어 반환
print(doc6)     #한건만 출력됨

# 여러건의 회원정보가 저장된 파일 읽어오기 4
with open('sungjuk.dat', encoding='UTF-8') as f:
    doc7 = []
    while True:
        line = f.readline()
        if not line:
            break
        doc7.append(line) # 행 단위로 하나씩 읽어 리스트에 저장
print(doc7)

# 여러건의 회원정보가 저장된 파일 읽어오기 5
with open('sungjuk.dat', encoding='UTF-8') as f:
    doc7 = []
    while True:
        line = f.readline()
        if not line:
            break
        item = line.split(',') # 각 행의 자료를 구분자로 분리해서 리스트로 저장
        out = f'{item[0]} {item[1]} {item[2]} {item[3]}'
        print(out, end=' ')

# 앞 예제에서 파일로 저장한 성적데이터를 다음과 같은 형태로 화면에 출력
# 이름 : abc, 국어 : 99, 영어 : 87, 수학 : 66
with open('sungjuk.dat', encoding='UTF-8') as f:
    doc7 = []
    while True:
        line = f.readline()
        if not line:
            break
        item = line.split(',') # 각 행의 자료를 구분자로 분리해서 리스트로 저장
        out = f'이름 : {item[0]}, 국어 : {item[1]}, 영어 : {item[2]}, 수학 : {item[3]}'
        print(out, end=' ')