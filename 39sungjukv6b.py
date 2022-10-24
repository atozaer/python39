# json 모듈을 이용한 성적처리 프로그램
# 성적 처리 프로그램의 모든 함수들은
# sungjukv5lib.py 에 작성하고 모듈명은 sjv5 로 줄여서 사용함
import sungjukv6blib as sjv6b

# 프로그램 주 실행부

# 프로그램 시작 전 데이터 초기화
sjv6b.loadSungJuk()
while True:
    # 메뉴표시 및 값 입력
    sjv6b.displayMenu()
    menu = input("메뉴를 선택하세요 => ")

    if menu == '1': sjv6b.addSungJuk()
    elif menu == '2': sjv6b.readSungJuk()
    elif menu == '3': sjv6b.readOneSungJuk()
    elif menu == '4': sjv6b.modifySungJuk()
    elif menu == '5': sjv6b.removeSungJuk()
    elif menu == '0': break
    else: print('잘못된 번호를 입력하였습니다')
