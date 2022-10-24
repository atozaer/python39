# csv 모듈을 이용한 성적처리 프로그램
# 성적 처리 프로그램의 모든 함수들은
# sungjukv5lib.py 에 작성하고 모듈명은 sjv5 로 줄여서 사용함
import sungjukv7lib as sjv7
import awsdbinfo

# 프로그램 주 실행부
while True:
    # 메뉴표시 및 값 입력
    sjv7.displayMenu()
    menu = input("메뉴를 선택하세요 => ")

    if menu == '1': sjv7.addSungJuk()
    elif menu == '2': sjv7.readSungJuk()
    elif menu == '3': sjv7.readOneSungJuk()
    elif menu == '4': sjv7.modifySungJuk()
    elif menu == '5': sjv7.removeSungJuk()
    elif menu == '0':
        # # 메모리에 존재하는 성적데이터를 파일에 저장
        # sjv6.saveSungJuk()
        break
    else: print('잘못된 번호를 입력하였습니다')