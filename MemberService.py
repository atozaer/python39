from MemberVO import MemberVO

class MemberService:

    @staticmethod
    def register_member():
        print('==========회원가입==========')
        userid = input('아이디 : ')
        passwd = input('비밀번호 : ')
        name = input('이름 : ')
        email = input('이메일 : ')
        mileage = int(input('마일리지 : '))

        member = MemberVO(userid, passwd, name, email, mileage)

        return member

    @staticmethod
    def process_member_grade(mvo):
        if mvo.mileage >= 10000:
            mvo.grade = 'vip'
        elif mvo.mileage >= 7000:
            mvo.grade = 'gold'
        elif mvo.mileage >= 4000:
            mvo.grade = 'silver'
        elif mvo.mileage >= 1000:
            mvo.grade = 'bronze'
        else:
            mvo.garade = 'member'
