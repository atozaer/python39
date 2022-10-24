from SungJukVO import SungJukVO
from SungJukv8DAO import SungJukv8DAO as sjdao


class SungJukv8Lib:
    # 함수 정의부
    # private function으로 선언
    @staticmethod
    def __input_sungjuk():
        name = input('이름은?')
        kor = int(input('국어 점수는?'))
        eng = int(input('영어 점수는?'))
        mat = int(input('수학 점수는?'))

        return SungJukVO(name, kor, eng, mat)

    # private function으로 선언
    @staticmethod
    def __compute_sungjuk(sj):
        sj.tot = sj.kor + sj.eng + sj.mat
        sj.avg = sj.tot / 3
        sj.grd = '가'

        if sj.avg >= 90:
            sj.grd = '수'
        elif sj.avg >= 80:
            sj.grd = '우'
        elif sj.avg >= 70:
            sj.grd = '미'
        elif sj.avg >= 60:
            sj.grd = '양'

    @staticmethod
    def display_menu():
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

        return print(main_menu)

    @staticmethod
    def add_sungjuk():
        # 성적 데이터 입력받기
        sj = SungJukv8Lib.__input_sungjuk()

        # 성적처리
        SungJukv8Lib.__compute_sungjuk(sj)

        # 처리된 성적데이터를 sungjuk 테이블에 저장
        if sjdao.insert_sungjuk(sj) > 0:
            print('성적 데이터 추가 완료!')

    @staticmethod
    def read_sungjuk():
        hdr = '이름 국어 영어 수학\n'
        hdr += '-----------------'
        print(hdr)

        result = ''
        for row in sjdao.select_sungjuk():
            result += f'{row[0]} {row[1]} {row[2]} {row[3]}\n'
        print(result)

    @staticmethod
    def read_one_sungjuk():
        name = input('조회할 학생의 이름은?')

        hdr = '이름 국어 영어 수학 총점 평균 학점\n'
        hdr += '---------------------------------'
        print(hdr)

        row = sjdao.select_one_sungjuk(name)

        result = f'{row[1]} {row[2]} {row[3]} {row[4]} {row[5]} {row[6]:.1f} {row[7]}'
        print(result)


    def modify_sungjuk():
        name = input('수정할 학생 이름은?')

        sj = sjdao.select_one_sungjuk(name)

        # 새로운(기존) 값을 입력받음
        kor = int(input(f'새로운 국어는? {sj[2]}'))
        eng = int(input(f'새로운 영어는? {sj[3]}'))
        mat = int(input(f'새로운 수학은? {sj[4]}'))

        # 다시 성적 처리
        sj = SungJukVO(name, kor, eng, mat)
        SungJukv8Lib.__compute_sungjuk(sj)

        # 새롭게 입력된 데이터를 기존 성적데이터에 반영함
        cnt = sjdao.update_sungjuk(sj)

        if cnt > 0:
            print('성공적으로 수정되었습니다.')

    @staticmethod
    def remove_sungjuk():

        name = input('삭제할 데이터의 학생 이름은?')

        cnt = sjdao.delete_sungjuk(name)
        if cnt > 0 :
            print('성공적으로 수정되었습니다.')
