# Set ADT 구현

class SetADT:

    def __init__(self):
        self.items = []   # 데이터를 저장하는 리스트

    def isEmpty(self):
        return len(self.items) == 0

    def isFull(self):
        return False   # 파이썬은 크기 제한 없음

    def size(self):
        return len(self.items)

    def contain(self, e):
        return e in self.items

    def insert(self, e):
        if not self.contain(e):       # 중복이면 삽입 안 함
            self.items.append(e)

    def delete(self, e):
        if self.contain(e):
            self.items.remove(e)
            return e
        return None

    def union(self, setB):            # 합집합 A ∪ B
        result = SetADT()
        for e in self.items:
            result.insert(e)
        for e in setB.items:
            result.insert(e)
        return result

    def intersect(self, setB):        # 교집합 A ∩ B
        result = SetADT()
        for e in self.items:
            if setB.contain(e):
                result.insert(e)
        return result

    def difference(self, setB):       # 차집합 A - B
        result = SetADT()
        for e in self.items:
            if not setB.contain(e):
                result.insert(e)
        return result

    def equals(self, setB):           # 두 집합이 같은지 비교
        if self.size() != setB.size():
            return False
        for e in self.items:
            if not setB.contain(e):
                return False
        return True

    def display(self, msg="[Set]"):
        print(f"{msg} {self.items}")


# 예제
print("===== Set ADT 예제 =====\n")

# 집합 A, B 생성
A = SetADT()
B = SetADT()

# insert: 원소 추가
print("--- insert ---")
for e in [1, 2, 3, 4, 5]:
    A.insert(e)
for e in [3, 4, 5, 6, 7]:
    B.insert(e)
A.display("A:")
B.display("B:")

# 중복 삽입 확인
print("\n--- 중복 삽입 (A에 3 다시 삽입) ---")
A.insert(3)
A.display("A (변화 없음):")

# contain: 원소 포함 여부
print("\n--- contain ---")
print(f"A에 3이 있나? {A.contain(3)}")
print(f"A에 9가 있나? {A.contain(9)}")

# delete: 원소 삭제
print("\n--- delete (A에서 1 삭제) ---")
A.delete(1)
A.display("A:")

# union: 합집합
print("\n--- union: A ∪ B ---")
AuB = A.union(B)
AuB.display("A∪B:")

# intersect: 교집합
print("\n--- intersect: A ∩ B ---")
AnB = A.intersect(B)
AnB.display("A∩B:")

# difference: 차집합
print("\n--- difference: A - B ---")
AmB = A.difference(B)
AmB.display("A-B:")

# equals: 같은 집합인지
print("\n--- equals ---")
C = SetADT()
for e in [2, 3, 4, 5]:
    C.insert(e)
print(f"A == B? {A.equals(B)}")
print(f"A == C? {A.equals(C)}")

# isEmpty / size
print("\n--- isEmpty / size ---")
print(f"A가 비어있나? {A.isEmpty()}")
print(f"A의 크기: {A.size()}")

# display
print("\n--- display ---")
A.display("최종 A:")
B.display("최종 B:")