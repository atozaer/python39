# 내장함수
# don't reinvent the wheel
# 파이썬에서 활용빈도 높은 기능을 함수로 미리 작성해두었음
# 이러한 함수를 사용할때는 특별한 지시문 필요 X

# 숫자관련
abs(-10)  # 절대값
abs(10)

sum([10, 20, 30])  # 요소의 총합 계산

max([10, 20, 30])  # 최대값 출력
min([10, 20, 30])  # 최소값 출력

round(34.56)  # 반올림
round(34.46)

# 자료형 관련
type(10)
type(10.5)
type(True)

# 변환 함수
ord('A')  # 유니코드 문자를 입력하면 코드값 출력
chr(65)  # chr = char    코드값을 입력하면 유니코드 문자 출력

# 정렬 함수
nums = ([10, 7, 15, 4])
sorted(nums)  # 오름차순 정렬
sorted(nums, reverse=True)  # 내림차순 정렬
list(reversed(nums))  # 순서 반전

# 묶음 함수 : zip
names = ['혜교', '지현', '수지']
ages = [33, 65, 77]

acter = list(zip(names, ages))
acter

# 함수를 조건식에 적용 - filter, map
# ex) 1~100사이 정수 중 짝수만 골라서 리스트에 저장
evens = []
for num in range(1, 100 + 1):
    if num % 2 == 0:
        evens.append(num)

print(evens)


# 짝수를 판별하는 코드를 함수로 캡슐화하고 다시 실행
def chkEven(num):
    isEven = False
    if num % 2 == 0: isEven = True

    return isEven


evens = []
for num in range(1, 100 + 1):
    if chkEven(num):
        evens.append(num)

# 짝수 판별하는 함수를 filter 함수로 재적용
# filter(적용할 함수, 함수를 적용할 대상)
# 리턴값 : 조건을 만족하는 값
evens1 = list(filter(chkEven, range(1, 100 + 1)))

# 짝수 판별하는 함수를 람다식으로 재적용
evens2 = list(filter(lambda x: x % 2 == 0, range(1, 100 + 1)))
print(evens2)

# ex) 1~10 사이 정수를 제곱해서 리스트에 저장 : 생산
squares1 = []
for num in range(1, 10 + 1):
    val = num ** 2
    squares1.append(val)

print(squares1)


# 정수를 제곱하는 함수를 만들어 재적용
def squrNum(num):
    return num ** 2


squares2 = []
for num in range(1, 10 + 1):
    squares2.append(squrNum(num))

print(squares2)

# 정수를 제곱하는 함수를 map 함수로 재적용
# map (적용할함수, 함수를적용할대상)
# 리턴 값 : 함수를 적용한 값
sqr1 = list(map(squrNum, range(1, 10 + 1)))
print(sqr1)

# 정수를 제곱하는 함수를 람다식으로 재적용
sqr2 = list(map(lambda x: x ** 2, range(1, 10 + 1)))
print(sqr2)



# 열거형 데이터 다루기 : enumerate
# 순서있는 객체들을 다룰때 인덱스를 포함시켜 객체를 리턴해 줌
print(names)

for idx, name in enumerate(names):
    print(idx, name)


# 29. 사용자로부터 소문자를 입력 받아 대문자로 출력하는 프로그램을 작성해보세요.
# 단, 소문자 이외의 숫자나 문자를 입력 받으면 “잘못 입력하셨습니다!!”라는 메시지를 출력하도록 합니다. (UpperCase)
# 문자 입력 시 input 사용
# A의 유니코드 값 : 65,      a의 유니코드 값 : 97

inputOrd = ord(input('영문 소문자를 입력해주세요 ==> '))

if 97 <= inputOrd < 123:
    inputOrd = ord(inputOrd)-32
    print(chr(inputOrd))
else:
    print('잘못 입력하셨습니다.')