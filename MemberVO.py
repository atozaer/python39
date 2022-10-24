class MemberVO:
    def __init__(self, userid, passwd, name, email, mileage):
        self.__userid = userid
        self.__passwd = passwd
        self.__name = name
        self.__email = email
        self.__mileage = mileage
        self.__grade = 'member'

    def __str__(self):
        result = f'{self.__userid} {self.__passwd} {self.__name} {self.__email} {self.__mileage} {self.__grade}'
        return result

    @property
    def userid(self):
        return self.__userid

    @userid.setter
    def userid(self, userid):
        self.__userid = userid

    @property
    def passwd(self):
        return self.__passwd

    @passwd.setter
    def passwd(self, passwd):
        self.__passwd = passwd

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def mileage(self):
        return self.__mileage

    @mileage.setter
    def mileage(self, mileage):
        self.__mileage = mileage

    @property
    def grade(self):
        return self.__grade

    @grade.setter
    def grade(self, grade):
        self.__grade = grade