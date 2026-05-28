# Stack ADT 구현
class Stack:

    def __init__(self):
        self.items = []   # 데이터를 저장하는 리스트

    def isEmpty(self):
        return len(self.items) == 0

    def isFull(self):
        return False      # 파이썬은 크기 제한 없음

    def size(self):
        return len(self.items)

    def push(self, e):
        self.items.append(e)       # 맨 뒤(top)에 추가

    def pop(self):
        if self.isEmpty():
            print("  [오류] 스택이 비어 있습니다. (underflow)")
            return None
        return self.items.pop()    # 맨 뒤(top)에서 꺼냄

    def peek(self):
        if self.isEmpty():
            print("  [오류] 스택이 비어 있습니다.")
            return None
        return self.items[-1]      # 꺼내지 않고 top만 확인

    def clear(self):
        self.items = []

    def display(self, msg="[Stack]"):
        print(f"{msg} {self.items}  ← top")


# 예제
print("===== Stack ADT 예제 =====\n")

s = Stack()

# push
print("--- push: A, B, C, D, E 순서로 삽입 ---")
for e in ["A", "B", "C", "D", "E"]:
    s.push(e)
s.display()

# peek
print(f"\n--- peek: top 확인 (꺼내지 않음) = {s.peek()} ---")
s.display("peek 후:")

# pop
print("\n--- pop: 두 번 꺼내기 ---")
print(f"  꺼낸 값: {s.pop()}")
print(f"  꺼낸 값: {s.pop()}")
s.display("pop 후:")

# isEmpty / isFull / size
print("\n--- 상태 확인 ---")
print(f"  isEmpty : {s.isEmpty()}")
print(f"  isFull  : {s.isFull()}")
print(f"  size    : {s.size()}")

# underflow 확인
print("\n--- underflow 확인 (빈 스택에서 pop) ---")
s.clear()
s.display("clear 후:")
s.pop()   # 오류 메시지 출력