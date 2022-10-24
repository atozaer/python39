# 파이썬으로 데이터 다루기 2 - insert
# 입력한 회원정보를 member 테이블에 저장
import sqlite3

# 회원정보 입력받기
userid = input('아이디는?')
passwd = input('비밀번호는?')
name = input('이름은?')
email = input('이메일은?')

conn = sqlite3.connect('c:/Java/bigdata.db')
cur = conn.cursor()

# 아래 방식은 비추 - SQL injection 공격의 위험 존재
# sql = 'insert into member values ('+userid+', '+passwd+', '+name+', '+email+')'

# sql = f' insert into member values ({userid},{passwd},{name},{email}) '

# 매개변수 placeholder(?)를 이용해서 실제 값 지정
sql = f' insert into member values (?,?,?,?) '
params = (userid, passwd, name, email)
cur.execute(sql, params)
conn.commit()           # 테이블 값에 저장하기위해 commit 호출
print(cur.rowcount, '행이 추가됨!')

cur.close()
conn.close()

