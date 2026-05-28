# DataStructure - List

Python을 이용하여 List ADT를 구현한 프로젝트입니다.

배열 기반 리스트(ArrayList)와 연결 리스트(LinkedList)를 직접 구현하여 자료구조의 동작 원리를 학습하는 것을 목표로 합니다.

---

## 구현 내용

이 프로젝트에서는 두 가지 방식의 리스트를 구현하였습니다.

### 1. ArrayList

파이썬의 기본 리스트를 이용한 배열 기반 리스트 구현입니다.

#### 주요 기능

* 데이터 추가 (`append`)
* 특정 위치 삽입 (`insert`)
* 데이터 삭제 (`delete`)
* 특정 위치 데이터 조회 (`getEntry`)
* 데이터 검색 (`find`)
* 데이터 교체 (`replace`)
* 정렬 (`sort`)
* 리스트 초기화 (`clear`)
* 리스트 출력 (`display`)

---

### 2. LinkedList

Node 클래스를 이용한 연결 리스트 구조 구현입니다.

각 노드는 데이터와 다음 노드를 가리키는 링크를 가지고 있습니다.

#### 주요 기능

* 노드 추가 (`append`)
* 노드 삭제 (`delete`)
* 특정 위치 데이터 조회 (`getEntry`)
* 데이터 검색 (`find`)
* 데이터 교체 (`replace`)
* 리스트 초기화 (`clear`)
* 리스트 출력 (`display`)

---

## 클래스 구조

```text
ArrayList
 └─ Python List 기반 구현

Node
 ├─ data
 └─ link

LinkedList
 └─ Node를 연결하여 구현
```

---

## 실행 예제

프로그램에서는 다음과 같은 기능들을 테스트합니다.

### ArrayList 테스트

* 데이터 추가
* 특정 위치 삽입
* 데이터 조회
* 데이터 검색
* 데이터 교체
* 데이터 삭제
* 정렬
* 리스트 초기화

### LinkedList 테스트

* 노드 추가
* 데이터 조회
* 데이터 검색
* 데이터 교체
* 노드 삭제
* 리스트 초기화

---

# DataStructure - Line Editor

Python과 Flet GUI 라이브러리를 이용하여 구현한 라인 편집기(Line Editor) 프로젝트입니다.

ArrayList 자료구조를 기반으로 문서의 각 줄(Line)을 관리하며, GUI 환경에서 삽입, 삭제, 수정, 저장 등의 기능을 제공합니다.

---

## 프로젝트 개요

이 프로젝트는 자료구조의 List ADT를 실제 프로그램 형태로 활용하기 위해 제작되었습니다.

문서의 각 줄을 리스트 형태로 저장하고 관리하며, 사용자는 GUI 버튼을 통해 문서 내용을 편집할 수 있습니다.


## 주요 기능

### 문서 편집 기능

| 기능           | 설명                  |
| ------------ | ------------------- |
| 삽입 (Insert)  | 원하는 위치에 새로운 라인 추가   |
| 삭제 (Delete)  | 특정 라인 삭제            |
| 변경 (Replace) | 특정 라인 내용 수정         |
| 출력 (Print)   | 현재 문서 내용 출력         |
| 저장 (Save)    | 문서를 test.txt 파일로 저장 |
| 불러오기 (Load)  | test.txt 파일 내용 불러오기 |
| 종료 (Quit)    | 프로그램 종료             |

---

## 자료구조 구현

프로그램 내부에서는 ArrayList 클래스를 이용하여 문서 내용을 저장합니다.

```text id="brvq0z"
문서
 ├─ 1번째 줄
 ├─ 2번째 줄
 ├─ 3번째 줄
 └─ ...
```

각 줄(Line)은 리스트의 원소(Element)로 관리됩니다.

---

## GUI 구성

프로그램은 Flet GUI를 이용하여 다음 요소들로 구성됩니다.

* 행 번호 입력 필드
* 내용 입력 필드
* 기능 버튼
* 현재 문서 출력 영역
* 상태 메시지 출력

---

## 실행 방법

### 1. Flet 설치

```bash id="jlwmjg"
pip install flet
```

---

---

## 파일 저장 방식

프로그램은 `test.txt` 파일을 이용하여 문서를 저장하고 불러옵니다.

* 저장 시: 현재 문서를 test.txt에 기록
* 불러오기 시: test.txt 내용을 리스트에 로드

---

## 실행 화면 예시

* 라인 삽입
* 라인 삭제
* 문서 출력
* 파일 저장 및 불러오기
* GUI 기반 문서 편집 기능 제공


# DataStructure - Set ADT

Python을 이용하여 Set ADT(Abstract Data Type)를 구현한 프로젝트입니다.

집합(Set)의 기본 특징인 중복 없는 데이터 저장과 집합 연산(합집합, 교집합, 차집합)을 직접 구현하여 자료구조의 동작 원리를 학습하는 것을 목표로 합니다.

---

## 프로젝트 개요

집합(Set)은 중복된 데이터를 허용하지 않으며, 원소 사이에 순서가 없는 자료구조입니다.

본 프로젝트에서는 Python 리스트를 기반으로 Set ADT를 직접 구현하였으며, 집합의 주요 연산들을 클래스 형태로 구현하였습니다.

---

## Set ADT 특징

* 원소의 중복을 허용하지 않음
* 원소 간 순서가 없음
* 집합 연산 가능

  * 합집합 (Union)
  * 교집합 (Intersection)
  * 차집합 (Difference)

---

## 구현 기능

| 함수               | 설명             |
| ---------------- | -------------- |
| isEmpty()        | 집합이 비어있는지 확인   |
| isFull()         | 집합이 가득 찼는지 확인  |
| size()           | 집합 원소 개수 반환    |
| contain(e)       | 특정 원소 포함 여부 확인 |
| insert(e)        | 원소 삽입          |
| delete(e)        | 원소 삭제          |
| union(setB)      | 합집합 생성         |
| intersect(setB)  | 교집합 생성         |
| difference(setB) | 차집합 생성         |
| equals(setB)     | 두 집합 비교        |
| display()        | 집합 출력          |

---

## 클래스 구조

```text id="rmz8ea"
SetADT
 ├─ insert()
 ├─ delete()
 ├─ contain()
 ├─ union()
 ├─ intersect()
 ├─ difference()
 ├─ equals()
 └─ display()
```

---

## 주요 집합 연산

### 1. 합집합 (Union)

```text id="7byqje"
A ∪ B
```

두 집합의 모든 원소를 포함하는 새로운 집합을 생성합니다.

---

### 2. 교집합 (Intersection)

```text id="8sm2n9"
A ∩ B
```

두 집합에 공통으로 존재하는 원소만 저장합니다.

---

### 3. 차집합 (Difference)

```text id="j04ecl"
A - B
```

A에는 존재하지만 B에는 존재하지 않는 원소를 저장합니다.

---

## 실행 예제

프로그램에서는 다음 기능들을 테스트합니다.

* 원소 삽입
* 중복 삽입 확인
* 원소 포함 여부 검사
* 원소 삭제
* 합집합 계산
* 교집합 계산
* 차집합 계산
* 집합 비교
* 집합 크기 확인

---

## 예제 출력

```text id="4kk2fr"
A: [1, 2, 3, 4, 5]
B: [3, 4, 5, 6, 7]

A∪B: [1, 2, 3, 4, 5, 6, 7]
A∩B: [3, 4, 5]
A-B: [1, 2]
```

---

## 프로젝트 목적

이 프로젝트를 통해 다음 내용을 학습할 수 있습니다.

* Set ADT의 구조와 특징
* 중복 없는 데이터 관리 방법
* 집합 연산 알고리즘
* Python 클래스 기반 자료구조 구현
* 자료구조의 추상 자료형(ADT) 개념 이해

---

# DataStructure - Stack ADT

Python을 이용하여 Stack ADT(Abstract Data Type)를 구현한 프로젝트입니다.

스택(Stack)의 기본 특징인 LIFO(Last In First Out) 구조를 직접 구현하여 자료구조의 동작 원리를 학습하는 것을 목표로 합니다.

---

## 프로젝트 개요

스택(Stack)은 가장 마지막에 들어간 데이터가 가장 먼저 나오는 선형 자료구조입니다.

본 프로젝트에서는 Python 리스트를 기반으로 Stack ADT를 직접 구현하였으며, 스택의 기본 연산들을 클래스 형태로 구현하였습니다.

---

## Stack 특징

* 후입선출(LIFO : Last In First Out) 구조
* 데이터 삽입과 삭제는 top에서만 수행
* 가장 최근에 삽입된 데이터가 가장 먼저 제거됨

---

## 구현 기능

| 함수        | 설명              |
| --------- | --------------- |
| isEmpty() | 스택이 비어있는지 확인    |
| isFull()  | 스택이 가득 찼는지 확인   |
| size()    | 스택 원소 개수 반환     |
| push(e)   | top에 데이터 삽입     |
| pop()     | top 데이터 제거 및 반환 |
| peek()    | top 데이터 확인      |
| clear()   | 스택 초기화          |
| display() | 스택 출력           |

---

## 클래스 구조

```text id="6q6c3j"
Stack
 ├─ push()
 ├─ pop()
 ├─ peek()
 ├─ size()
 ├─ clear()
 └─ display()
```

---

## 주요 연산 설명

### 1. Push

```text id="bxm3ma"
push(A)
push(B)
push(C)
```

새로운 데이터를 스택의 top 위치에 삽입합니다.

---

### 2. Pop

```text id="42x0o7"
pop()
```

스택의 top 데이터를 제거하고 반환합니다.

가장 마지막에 삽입된 데이터가 먼저 제거됩니다.

---

### 3. Peek

```text id="v1u9gd"
peek()
```

top 데이터를 제거하지 않고 확인만 수행합니다.

---

## 실행 예제

프로그램에서는 다음 기능들을 테스트합니다.

* push 연산
* peek 연산
* pop 연산
* 스택 상태 확인
* underflow 확인
* clear 연산

---

## 예제 출력

```text id="e0bg5h"
[Stack] ['A', 'B', 'C', 'D', 'E'] ← top

peek = E

꺼낸 값: E
꺼낸 값: D

[Stack] ['A', 'B', 'C'] ← top
```

---

## Underflow 처리

빈 스택에서 pop()을 수행하면 underflow 오류 메시지를 출력하도록 구현하였습니다.

```text id="ehqjaf"
[오류] 스택이 비어 있습니다. (underflow)
```

---

## 프로젝트 목적

이 프로젝트를 통해 다음 내용을 학습할 수 있습니다.

* Stack ADT의 구조와 특징
* LIFO 구조의 동작 원리
* 스택 기반 자료구조 구현
* Python 클래스 기반 자료구조 구현
* underflow 예외 상황 처리
