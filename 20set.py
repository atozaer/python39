# 집합(set)
# 비순차 열거형 자료구조
# 데이터가 저장된 순서를 기억하지 않음 (인덱스 사용x)
# 단, 집합을 리스트나 튜플로 변환하면 사용가능
# 입력된 데이터의 중복을 허용하지 않음
# 선언방법은 값들을 {}안에 정의하고 사용
import random

# 집합 선언
# nums = {1,2,3,4,5}

# 집합 출력 1 / 인덱스조회 불가
# print(nums[0])

# 집합 출력 2 / 순차조회 불가
# for i in range(len(nums)):
#     print(nums[i])

# 집합 출력 3 / 하나씩 열거해가며 조회 가능
# for num in nums:
#     print(num, end=' ')

# 집합 동적 생성
# nums = {} <- 딕셔너리 자료형으로 인식
# nums = set()

# nums.add(10)
# nums.add(20)
# nums.add(30)
# nums.add(30)

# print(nums)

# 집합 값 제거 : remove(값)
# nums.remove(20)
# print(nums)

# 집합 값 수정 : 기본적으로는 불가, 단 리스트 변환시 가능
# nums = list(nums)
# nums[0] = 999
# nums = set(nums)

# ex) 로또 645 : 1 ~ 45 사이 임의이 숫자 6개 생성 1
# 단, set을 이용해서 같은 숫자가 출현하지 않도록 작성

# lotto = set()
# while len(lotto)<=6:
#     lotto.add(random.randint(1, 45))
# print(lotto)

# ex) 로또 645 : 1 ~ 45 사이 임의이 숫자 6개 생성 2
# 단, list를 이용해서 같은 숫자가 출현하지 않도록 작성

# import random as rnd
# lotto = []
# while len(lotto) < 6:
#     num = rnd.randint(1, 45) # 로또 번호 생성
#     if not(num in lotto): lotto.append(num) # 배열내 랜덤 생성 된 값 존재 여부에 따라 값 추가 결정
# print(lotto)

# ex) 로또 645 : 1 ~ 45 사이 임의이 숫자 6개 생성 3
# 단, list를 이용해서 같은 숫자가 출현하지 않도록 작성

lottos = list(range(1, 45+1))

# 로또 번호를 뽑을 인덱스를 난수로 생성
for _ in range(6):
    random.shuffle(lottos)
    idx = random.randint(0, len(lottos)-1)
    print(lottos[idx], end=' ')
    # lottos.remove(lottos[idx])       # 비복원추출
    lottos.pop(idx)
    print(lottos)


