# 회원가입을 처리하는 클래스 생성
# MemberVO :
#     userid, passwd, name, email, milege, grade
# MemberService :
#  registerMember  : 회원 정보 입력
#  processMemberGrade : 마일리지에 따라 회원 등급 결정
#      vip : 마일리지 - 10000이상
#      gold : 마일리지 - 7000이상
#      silver : 마일리지 - 4000이상
#      bronze : 마일리지 - 1000이상
#      member : 그외

from MemberService import MemberService as mbsr


mb = mbsr.register_member()
mbsr.process_member_grade(mb)
print(mb)