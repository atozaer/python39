# 성적처리프로그램 v3

# 2차원 리스트와 dict를 이용한 성적처리 프로그램
# 성적 데이터 저장할 변수 선언

sjs = []

# 프로그램 메뉴 출력을 위한 변수 선언
line = "-" * 30
main_menu = f"""
성적처리프로그램 v3
{line:s}
  1. 성적 데이터 추가
  2. 성적 데이터 조회
  3. 성적 데이터 상세조회
  4. 성적 데이터 수정
  5. 성적 데이터 삭제
  0. 프로그램 종료
{line:s}"""
while True:
    print(main_menu)
    selectMenu = input("메뉴를 선택하세요 => ")

    if selectMenu == '1':
        name = input('이름은?')
        kor = int(input('국어 점수는?'))
        eng = int(input('영어 점수는?'))
        mat = int(input('수학 점수는?'))

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

        sj = {}
        sj = {'name': name, 'kor': kor, 'eng': eng, 'mat': mat, 'tot': tot, 'avg': avg, 'grd': grd}

        sjs.append(sj)

        print('성적데이터 추가 완료!')

    elif selectMenu == '2':
        hdr = '이름 국어 영어 수학\n'
        hdr += '-----------------'
        print(hdr)

        for sj in sjs:
            print(f'{sj["name"]} {sj["kor"]} {sj["eng"]} {sj["mat"]}', end=' ')
            print()

        input('성적 데이터 조회 완료!')

    elif selectMenu == '3':  # 이름으로 검색 후 해당학생의 정보 모두 출력
        name = input('조회할 학생의 이름은?')

        sj = None
        for item in sjs:
            if item['name'] == name:
                sj = item

        hdr = '이름 국어 영어 수학 총점 평균 학점\n'
        hdr += '---------------------------------'
        print(hdr)

        for k in sj.keys():
            print(sj.get(k), end=' ')
        print()
        input('성적 데이터 상세조회')

    elif selectMenu == '4':
        name = input('수정할 학생 이름은?')

        sj = None
        for item in sjs:
            if item['name'] == name:
                sj = item

        # 기존에 위치에 다시저장
        idx = None
        for i in range(len(sjs)):
            if (sjs[i])['name'] == name:
                idx = i

                # 새로운(기존) 값을 입력받음
                kor = int(input(f'새로운 국어는? {sj["kor"]}'))
                eng = int(input(f'새로운 영어는? {sj["eng"]}'))
                mat = int(input(f'새로운 수학은? {sj["mat"]}'))

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
                break

        # 값 다시저장
        sj = {'name': name, 'kor': kor, 'eng': eng, 'mat': mat, 'tot': tot, 'avg': avg, 'grd': grd}

        sjs[idx] = sj

        print('성적 데이터 수정')

    elif selectMenu == '5':
        name = input('삭제할 데이터의 학생 이름은?')

        idx = None
        for i in range(len(sjs)):
            item = sjs[i]
            if item['name'] == name:
                idx = i

        sjs.pop(idx)

        input('성적 데이터 삭제')

    elif selectMenu == '0':
        print('프로그램 종료')
        break
    else:
        print('잘못된 번호를 입력하셨습니다.')
