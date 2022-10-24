# 마리아DB로 데이터 다루기 1 - select
# pymysql 모듈을 먼저 설치

import pymysql
#
# url = 'bigdata.cg4bbtswhlwt.ap-northeast-2.rds.amazonaws.com'
# dbid = 'admin'
# passwd = 'Bigdata_2022'
# dbname = 'bigdata'
#
# conn = pymysql.connect(host=url, user=dbid, password=passwd, database=dbname, charset='UTF8')
# cur = conn.cursor()
#
# sql = ' select userid, passwd, name, email from member '
#
# cur.execute(sql)
#
# result = ''
# rows = cur.fetchall()
# for row in rows:
#     result += f'{row[0]},{row[1]},{row[2]},{row[3]}\n'
#
# cur.close()
# conn.close()
# print(result)


# 마리아DB로 데이터 다루기 2 - insert
import pymysql

# 회원정보 입력받기
userid = input('아이디는?')
passwd = input('비밀번호는?')
name = input('이름은?')
email = input('이메일은?')

url = 'bigdata.cg4bbtswhlwt.ap-northeast-2.rds.amazonaws.com'
dbid = 'admin'
passwd = 'Bigdata_2022'
dbname = 'bigdata'

conn = pymysql.connect(host=url, user=dbid, password=passwd, database=dbname, charset='UTF8')
cur = conn.cursor()

# 아래 방식은 비추 - SQL injection 공격의 위험 존재
# sql = 'insert into member values ('+userid+', '+passwd+', '+name+', '+email+')'

# sql = f' insert into member values ({userid},{passwd},{name},{email}) '

# 매개변수 placeholder(?)를 이용해서 실제 값 지정
sql = f' insert into member(userid, passwd, name, email) values (%s,%s,%s,%s) '
params = (userid, passwd, name, email)
cur.execute(sql, params)
conn.commit()           # 테이블 값에 저장하기위해 commit 호출
print(cur.rowcount, '행이 추가됨!')

cur.close()
conn.close()