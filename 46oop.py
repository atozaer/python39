# IT 인프라
# 엔터프라이즈 IT 환경을 운영하고 관리하는 데 필요한 구성 요소
# IT 서비스 및 솔루션을 제공하기 위해
# 필요한 IT 환경(서비스 및 플랫폼)을 구축, 개발, 운영하기 위해 필요한 모든 구성요소
# 플랫폼 - 하드웨어, 네트워킹요소, 데이터 스토리지
# 서비스 - 운영체제, 소프트웨어

# IT 인프라 구성 방식
# 집약형 - 한대의 시스템으로 모든 기능을 해결
# 분산형 - 여러 대의 시스템을 조합해서 하나의 시스템으로 구축(클러스터링)

# 분산형 아키텍처
# 서버별로 다른 역할을 하도록 시스템을 수직으로 확장하는 구조
# c/s, 3-tier

# 수평 분할형 아키텍처
# 용도가 같은 서버를 늘려나가는 방식 - sharding, Partitioning

# 스탠바이형 아키텍처
# 물리 서버를 최소 두 대를 준비하여
# 한 대가 고장 나면 가동 중인 소프트웨어를
# 다른 한 대로 옮겨서 운영하는 방식
# 스탠바이, HA(High Availiability), Active-Standby 라고도 함

# client-server : 화면 표시나 단순한 계산은 클라이언트에서 실행하고,
# 필요한 경우(데이터 요청 등) 서버에서 데이터 요청

# 3-tier 아키텍처
# 응용프로그램을 3개의 논리적 및 물리적 컴퓨팅 계층으로 구성하는 소프트웨어 아키텍처
# '프리젠테이션 계층', 데이터를 처리하는 '애플리케이션 계층',
# 그리고 애플리케이션과 연관된 데이터를 저장 및 관리하는 '데이터 계층'으로 구성
# 보다 신속한 개발, 확장성 개선, 안정성 향상, 보안성 강화

# 프레젠테이션 계층 (Presentation Tier)
# 일반 사용자가 애플리케이션과 상호작용하는 애플리케이션의
# 사용자 인터페이스 및 통신 계층
# 주요 목적은 정보를 표시하고 사용자로부터 정보를 수집하는 것

# 애플리케이션 계층
# 프리젠테이션 계층에서 수집된 정보를
# 다양한 비즈니스 규칙(로직)을 이용해서 처리함
# 프레젠테이션 계층에서 온 요청을 받아,
# 요구에 필요한 데이터를 데이터 계층에 요청하며
# 전달 받은 데이터를 특정 처리 및 가공을 하여
# 프레젠테이션 계층에 전달하는 것을 담당

# 데이터 계층
# 어플리케이션 계층의 요청에 따라 데이터 입출력 처리
# 데이터베이스와 데이터베이스에 접근하여 데이터를
# 읽거나 쓰는 것을 관리하는 계층

# 소프트웨어의 좋은 설계
# 유지보수가 용이해야 함
# 높은 응집도와 낮은 결합도를 가지도록 요소(모듈)를 적절히 배치하는 것
# - 소프트웨어 설계 품질을 판단하는 기준
# 모듈: 크기와 상관없이 클래스나 패키지,
# 라이브러리와 같이 프로그램을 구성하는 임의의 요소를 의미

# 결합도Coupling: 다른 모듈과의 상호 의존성 정도,
# 모듈 간의 의존이 심하면 모듈의 독립성이 악화
# 모듈을 수정하려고 하는데, 다른 모듈이 영향을 받으면 수정하기 힘들 테니,
# 그 영향이 거의 없을수록 부담없이 수정이 가능

# 응집도Cohesion: 모듈에 포함된 내부 요소들이
# 하나의 책임/목적을 수행하기 위해 얼마나 잘 연관되었나의 정도
# 응집도가 높으면 수정해야 될 코드가 한 군데에 모여있기 때문에
# 하나(최소한)의 모듈만 분석해서 수정하면 되니 유지보수 하기 좋음

# 파이썬 객체지향 프로그래밍
# OOP : object oriented programming
# 프로그램을 명령어들의 단순 묶음이라고 보는 시각에서
# 벗어나 독립된 객체들의 모음이라고 보는 시각에 근거해서
# 프로그래밍하는 패러다임

# 프로그램을 보다 유연하게 작성할 수 있고
# 프로그램 코드의 재사용을 높일수 있으며
# 대규모 소프트웨어 개발시 유지보수가 용이해짐

# 프로그램의 각 구성요소를 실제세계의 객체와 유사하게
# 디자인해서 클래스로 정의하는 것에 중점을 둠

# ex) 성적처리 프로그램
# 이름,국어,영어,수학을 입력하면
# 총점,평균,학점을 출력

# 성적 입력
name = input('이름은 ?')
kor = int(input('국어는 ?'))
eng = int(input('영어는 ?'))
mat = int(input('수학은 ?'))

# 성적 처리
tot = kor + eng + mat
avg = tot / 3
grd = '가'
if (avg >= 90):
    grd = '수'
elif (avg >= 80):
    grd = '우'
elif (avg >= 70):
    grd = '미'
elif (avg >= 60):
    grd = '양'

# 결과 출력
print('입력:%s %s %s %s' % (name, kor, eng, mat))
print('결과:%s %.1f %s' % (tot, avg, grd))


# ex) 성적처리 프로그램 II
# 함수 기반 프로그래밍 : 처리코드들을 하나의 이름으로 묶음
def readSungJuk():
    name = input('이름은 ?')
    kor = int(input('국어는 ?'))
    eng = int(input('영어는 ?'))
    mat = int(input('수학은 ?'))

    return name, kor, eng, mat


def computeSungJuk(kor, eng, mat):
    tot = kor + eng + mat
    avg = tot / 3
    grd = '가'
    if (avg >= 90):
        grd = '수'
    elif (avg >= 80):
        grd = '우'
    elif (avg >= 70):
        grd = '미'
    elif (avg >= 60):
        grd = '양'

    return tot, avg, grd


def printSungJuk(name, kor, eng, mat, tot, avg, grd):
    print('입력:%s %s %s %s' % (name, kor, eng, mat))
    print('결과:%s %.1f %s' % (tot, avg, grd))


# 프로그램 실행
name, kor, eng, mat = readSungJuk()
tot, avg, grd = computeSungJuk(kor, eng, mat)
printSungJuk(name, kor, eng, mat, tot, avg, grd)


# ex) 성적처리 프로그램 III
# 객체지향 프로그램 : 함수들과 관련된 변수들을 하나로 묶음
# 성적 데이터를 담고있는 클래스와
# 성적처리에 필요한 기능들로만 구성된 클래스로 나눠 작성

# OOP에서의 클래스 특성
# 1. 값만 저장하는 클래스 : VO, DTO
# 2. 기능만 저장하는 클래스 : DAO, BO
# 데이터베이스 연동 클래스 : CRUD 기능 지원
# 3. UI처리만 저장하는 클래스 : UO

# OOP 3대 특성
# 캡슐화
# 상속
# 다형성

# OOP 5대 원칙
# 결합도, 응집도
# SOLID


# 클래스 정의
# 클래스이름은 camel표기법으로 지음
# class 클래스명(상속여부):
#   생성자
#   setter/getter
#   메서드

# 1. 값만 저장하는 클래스 : VO
# 생성자 : __init__ (매직함수)
# private 멤버변수 선언
# setter/getter : @setter, @property ( @ : 데코레이터 )

class SungJukVO:
    # 생성자 : 클래스 객체 생성시 초기화 작업을 수행하는 함수
    # 생성자를 통해 멤버변수 선언 및 기본값을 지정할 수 있음
    # 변수선언 : self.변수명(public), self.__변수명(private)

    def __init__(self):
        self.__name = ''
        self.__kor = 0
        self.__eng = 0
        self.__mat = 0
        self.__tot = 0
        self.__avg = 0.0
        self.__grd = ''

    # settt/getter
    # @property를 먼저 정의하고, @setter를 정의해야 함
    # @property
    # def 멤버변수명(self)
    #     return self.멤버변수명

    # @멤버변수명.setter
    # def 멤버변수명(self, 멤버변수명):
    #     self.멤버변수명 = 멤버변수명
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def kor(self):
        return self.__kor

    @kor.setter
    def kor(self, kor):
        self.__kor = kor

    @property
    def eng(self):
        return self.__eng

    @eng.setter
    def eng(self, eng):
        self.__eng = eng

    @property
    def mat(self):
        return self.__mat

    @mat.setter
    def mat(self, mat):
        self.__mat = mat

    @property
    def tot(self):
        return self.__tot

    @tot.setter
    def tot(self, tot):
        self.__tot = tot

    @property
    def avg(self):
        return self.__avg

    @avg.setter
    def avg(self, avg):
        self.__avg = avg

    @property
    def grd(self):
        return self.__grd

    @grd.setter
    def grd(self, grd):
        self.__grd = grd


# 성적 객체 생성
# 클래스에 대한 객체 생성
# 변수명 = 클래스명()
sj = SungJukVO()

# 객체의 멤버 변수 접근 : 객체명.멤버변수명
# 멤버변수를 private로 선언(__변수명)하면
# 은닉변수가 되어 접근불가 - 캡슐화
# 이럴경우 setter/getter로 정의된 함수로만 접근 가능
sj.name = '혜교'
sj.kor = 99
sj.eng = 88
sj.mat = 77

print(sj.name, sj.kor, sj.eng, sj.mat)
