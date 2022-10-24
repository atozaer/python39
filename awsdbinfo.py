import pymysql

url = ''
userid = ''
passwd = ''
dbname = ''

def openConn():
    conn = pymysql.connect(host=url, user=userid, password=passwd, database=dbname, charset='utf8')

    cur = conn.cursor()

    return conn, cur

def closeConn(conn, cur):
    conn.close()
    cur.close()