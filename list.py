# List ADT 구현
# 1) ArrayList  : 배열(파이썬 리스트) 방식
# 2) LinkedList : 연결된 구조 방식

# 1. 배열 방식
class ArrayList:

    def __init__(self):
        self.items = []   # 데이터를 저장하는 리스트

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def insert(self, pos, e):
        self.items.insert(pos, e)

    def append(self, e):
        self.items.append(e)

    def delete(self, pos):
        return self.items.pop(pos)

    def getEntry(self, pos):
        return self.items[pos]

    def find(self, item):
        if item in self.items:
            return self.items.index(item)
        return None

    def replace(self, pos, item):
        self.items[pos] = item

    def sort(self):
        self.items.sort()

    def clear(self):
        self.items = []

    def display(self, msg="[ArrayList]"):
        print(msg, self.items)


# 2. 연결된 구조 방식
class Node:
    def __init__(self, data):
        self.data = data   # 데이터
        self.link = None   # 다음 노드 주소


class LinkedList:

    def __init__(self):
        self.head = None   # 첫 번째 노드 주소
        self.count = 0

    def isEmpty(self):
        return self.head is None

    def size(self):
        return self.count

    def append(self, e):
        new_node = Node(e)
        if self.isEmpty():             # 리스트가 비어있으면
            self.head = new_node
        else:                          # 마지막 노드 찾아서 연결
            node = self.head
            while node.link is not None:
                node = node.link
            node.link = new_node
        self.count += 1

    def delete(self, pos):
        if pos == 0:                   # 첫 번째 노드 삭제
            removed = self.head.data
            self.head = self.head.link
        else:                          # 중간 노드 삭제
            node = self.head
            for _ in range(pos - 1):
                node = node.link
            removed = node.link.data
            node.link = node.link.link
        self.count -= 1
        return removed

    def getEntry(self, pos):
        node = self.head
        for _ in range(pos):
            node = node.link
        return node.data

    def find(self, item):
        node = self.head
        idx = 0
        while node is not None:
            if node.data == item:
                return idx
            node = node.link
            idx += 1
        return None

    def replace(self, pos, item):
        node = self.head
        for _ in range(pos):
            node = node.link
        node.data = item

    def clear(self):
        self.head = None
        self.count = 0

    def display(self, msg="[LinkedList]"):
        items = []
        node = self.head
        while node is not None:
            items.append(node.data)
            node = node.link
        print(msg, items)


# 예제 1) ArrayList 사용
print("===== 예제 1: ArrayList =====")

al = ArrayList()

al.append(10)
al.append(20)
al.append(30)
al.display("추가 후:")

al.insert(1, 99)
al.display("인덱스 1에 99 삽입:")

print("인덱스 2의 값:", al.getEntry(2))
print("20의 위치:", al.find(20))

al.replace(0, 100)
al.display("인덱스 0을 100으로 교체:")

removed = al.delete(1)
print("인덱스 1 삭제, 삭제된 값:", removed)
al.display("삭제 후:")

al.sort()
al.display("정렬 후:")

print("비어있나?", al.isEmpty())
print("크기:", al.size())

al.clear()
al.display("초기화 후:")


# 예제 2) LinkedList 사용
print("\n===== 예제 2: LinkedList =====")

ll = LinkedList()

ll.append("A")
ll.append("B")
ll.append("C")
ll.display("추가 후:")

print("인덱스 1의 값:", ll.getEntry(1))
print("C의 위치:", ll.find("C"))

ll.replace(0, "Z")
ll.display("인덱스 0을 Z로 교체:")

removed = ll.delete(1)
print("인덱스 1 삭제, 삭제된 값:", removed)
ll.display("삭제 후:")

print("비어있나?", ll.isEmpty())
print("크기:", ll.size())

ll.clear()
ll.display("초기화 후:")