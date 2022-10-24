# 파이썬으로 데이터 다루기 4 - delete
# 삭제할 회원의 아이디를 입력받아 회원정보 삭제

import sqlite3

userid = input('삭제할 회원의 아이디는?')

conn = sqlite3.connect('C:/Java/bigdata.db')
cur = conn.cursor()

sql = ' delete from member where userid = :uid '
param = {'uid':userid}

cur.execute(sql,param)
print(cur.rowcount, '행이 삭제됨!')
conn.commit()

cur.close()
conn.close()
