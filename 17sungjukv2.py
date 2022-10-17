# 성적처리프로그램

# 성적 데이터 저장할 변수 선언
names = []
kors = []
engs = []
mats = []
tots = []
avgs = []
grds = []

# 프로그램 메뉴 출력을 위한 변수 선언
line = "-" * 30
main_menu = f"""
    성적처리프로그램
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

        if avg >= 90 :
            grd = '수'
        elif avg >= 80:
            grd = '우'
        elif avg >= 70:
            grd = '미'
        elif avg >= 60:
            grd = '양'

        names.append(name)
        kors.append(kor)
        engs.append(eng)
        mats.append(mat)
        tots.append(tots)
        avgs.append(avg)
        grds.append(grd)

        print('성적데이터 추가 완료!')

    elif selectMenu == '2':
        hdr =  '이름 국어 영어 수학\n'
        hdr += '-----------------'
        print(hdr)

        for i in range(len(names)):
            print(f'{names[i]}\t{kors[i]}\t{engs[i]}\t{mats[i]}')

        input('성적 데이터 조회 완료!')

    elif selectMenu == '3':
        print('성적 데이터 상세조회')

    elif selectMenu == '4':
        print('성적 데이터 수정')

    elif selectMenu == '5':
        print('성적 데이터 삭제')

    elif selectMenu == '0':
        print('프로그램 종료')
        break
    else:
        print('잘못된 번호를 입력하셨습니다.')
