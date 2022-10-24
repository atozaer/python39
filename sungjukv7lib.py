import pymysql
import awsdbinfo as db

sj = []


# 함수 정의부
def displayMenu():
    main_menu = f'''
    성적 처리프로그램 v7
    -----------------
    1. 성적 데이터 추가
    2. 성적 데이터 조회
    3. 성적 데이터 상세조회
    4. 성적 데이터 수정
    5. 성적 데이터 삭제
    0. 프로그램 종료
    -----------------'''
    print(main_menu)

    return str()


def inputSungJuk():
    name = input('이름은?')
    kor = int(input('국어 점수는?'))
    eng = int(input('영어 점수는?'))
    mat = int(input('수학 점수는?'))

    # sj = {'name': name, 'kor': kor, 'eng': eng, 'mat': mat}
    sj = [name, kor, eng, mat]

    return sj


def addSungJuk():
    # 성적 데이터 입력받기
    name, kor, eng, mat = inputSungJuk()

    # 성적처리
    tot, avg, grd = computeSungJuk(kor, eng, mat)
    print(tot, avg, grd)
    # 처리된 성적데이터를 sungjuk 테이블에 저장
    conn, cur = db.openConn()

    sql = " insert into sungjuk(name,kor,eng,mat,tot,avg,grd) values (%s,%s,%s,%s,%s,%s,%s) "
    params = (name, kor, eng, mat, tot, avg, grd)
    cur.execute(sql, params)
    conn.commit()
    print(cur.rowcount, '개의 성적 데이터가 추가됨!')

    db.closeConn(conn, cur)

    # input('성적 데이터 추가 완료!')


def readSungJuk():
    hdr = '이름 국어 영어 수학\n'
    hdr += '-----------------'
    print(hdr)

    conn, cur = db.openConn()

    sql = ' select name, kor, eng, mat from sungjuk order by sjno '
    cur.execute(sql)
    rows = cur.fetchall()

    db.closeConn(conn, cur)

    result = ''
    for row in rows:
        result += f'{row[0]} {row[1]} {row[2]} {row[3]}\n'
    print(result)


def readOneSungJuk():
    name = input('조회할 학생의 이름은?')

    hdr = '이름 국어 영어 수학 총점 평균 학점\n'
    hdr += '---------------------------------'
    print(hdr)

    conn, cur = db.openConn()

    sql = ' select * from sungjuk where name = %s '

    cur.execute(sql, [name])
    row = cur.fetchone()

    db.closeConn(conn, cur)

    result = f'{row[1]} {row[2]} {row[3]} {row[4]} {row[5]} {row[6]:.1f} {row[7]}'
    print(result)


def modifySungJuk():
    name = input('수정할 학생 이름은?')

    conn, cur = db.openConn()
    sql = ' select name, kor, eng, mat from sungjuk where name = %s '
    cur.execute(sql, [name])
    sj = cur.fetchone()
    db.closeConn(conn, cur)

    # 새로운(기존) 값을 입력받음
    kor = int(input(f'새로운 국어는? {sj[1]}'))
    eng = int(input(f'새로운 영어는? {sj[2]}'))
    mat = int(input(f'새로운 수학은? {sj[3]}'))

    # 다시 성적 처리
    sj = [name, kor, eng, mat]
    tot, avg, grd = computeSungJuk(kor, eng, mat)

    sj = sj + [tot, avg, grd]

    # 새롭게 입력된 데이터를 기존 성적데이터에 반영함
    conn, cur = db.openConn()
    sql = ' update sungjuk set kor=%(kr)s, eng=%(en)s, mat=%(mt)s, tot=%(tt)s, avg=%(av)s, grd=%(gd)s, regdate=current_timestamp where name = %(nm)s '

    params= dict(nm=sj[0], kr=sj[1], en=sj[2], mt=sj[3], tt=sj[4], av=sj[5], gd=sj[6])
    cur.execute(sql, params)

    cnt = cur.rowcount
    conn.commit()

    db.closeConn(conn, cur)

    if cnt > 0:
        print('성공적으로 수정되었습니다.')


def removeSungJuk():
    name = input('삭제할 데이터의 학생 이름은?')

    conn, cur = db.openConn()

    sql = ' delete from sungjuk where name = %s '
    cur.execute(sql, [name])

    cnt = cur.rowcount
    conn.commit()

    db.closeConn(conn, cur)

    if cnt > 0:
        print('성공적으로 삭제되었습니다.')


def computeSungJuk(kor, eng, mat):
    tot = kor + eng + mat
    avg = tot / 3
    grd = '가'

    if avg >= 90:
        grd = '수'
    elif avg >= 80:
        grd = '우'
    elif avg >= 70:
        grd = '미'
    elif avg >= 60:
        grd = '양'

    return tot, avg, grd
