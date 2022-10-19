# 모듈을 이용한 성적처리 프로그램
# 성적 처리 프로그램의 모든 함수들은
# sungjukv5lib.py 에 작성하고 모듈명은 sjv5 로 줄여서 사용함
import sungjukv5lib as sjv5

# 프로그램 주 실행부
while True:
    # 메뉴표시 및 값 입력
    menu = sjv5.displayMenu()

    if menu == '1': sjv5.addSungJuk()
    elif menu == '2': sjv5.readSungJuk()
    elif menu == '3': sjv5.readOneSungJuk()
    elif menu == '4': sjv5.modifySungJuk()
    elif menu == '5': sjv5.removeSungJuk()
    elif menu == '0': break
    else: print('잘못된 번호를 입력하였습니다')