# 파이썬으로 데이터 다루기 3 - update
# 수정할 회원의 아이디를 입력받아 회원정보 수정

import sqlite3

userid = input('수정할 회원 아이디는?')
passwd = input('비밀번호 수정 : ')
name = input('이름 수정 : ')
email = input('이메일 수정 : ')

conn = sqlite3.connect('C:/Java/bigdata.db')
cursor = conn.cursor()

# named parameter placeholder를 이요해서 실제 값 지정
sql = ' update member set passwd=:pwd, name=:name, email=:email where userid = :userid '

params = {'pwd':passwd,'name':name,'email':email,'userid':userid}
cursor.execute(sql,params)
print(cursor.rowcount, "행이 수정됨!")

conn.commit()

cursor.close()
conn.close()
