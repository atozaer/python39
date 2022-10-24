# 개선된 성적 클래스 - 생성자를 통해 변수 초기화
class SungJukVO:
    # 생성자
    def __init__(self, name, kor, eng, mat):
        self.__name = name
        self.__kor = kor
        self.__eng = eng
        self.__mat = mat
        self.__tot = 0
        self.__avg = 0.0
        self.__grd = ''

    # __str__ : 멤버변수들의 값을 문자열화 해서 객체 정보를 외부에 표현할 때 사용
    def __str__(self):
        self.computeSungJuk()

        result = f'{self.__name} {self.__kor} {self.__eng} {self.__mat} {self.__tot} {self.__avg} {self.__grd}'

        return result

    # 성적 처리
    def computeSungJuk(self):
        self.__tot = self.__kor + self.__eng + self.__mat
        self.__avg = self.__tot / 3
        self.__grd = '가'
        if self.__avg >= 90:
            self.__grd = '수'
        elif self.__avg >= 80:
            self.__grd = '우'
        elif self.__avg >= 70:
            self.__grd = '미'
        elif self.__avg >= 60:
            self.__grd = '양'


# 성적 객체 생성
sj = SungJukVO('혜교', 99, 88, 77)
print(sj)
