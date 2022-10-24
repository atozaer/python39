# csv 모듈을 이용한 성적처리 프로그램
# 성적 처리 프로그램의 모든 함수들은
# sungjukv8lib, SungJukv8DAO 에 작성하고 모듈명은 sjv8 로 줄여서 사용함
from sungjukv8lib import SungJukv8Lib as sjv8

# 프로그램 주 실행부
while True:
    # 메뉴표시 및 값 입력
    sjv8.display_menu()
    menu = input("메뉴를 선택하세요 => ")

    if menu == '1': sjv8.add_sungjuk()
    elif menu == '2': sjv8.read_sungjuk()
    elif menu == '3': sjv8.read_one_sungjuk()
    elif menu == '4': sjv8.modify_sungjuk()
    elif menu == '5': sjv8.remove_sungjuk()
    elif menu == '0': break
    else: print('잘못된 번호를 입력하였습니다')