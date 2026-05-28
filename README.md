# list.py

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

## 실행 방법

터미널에서 아래 명령어를 입력합니다.

```bash
python list.py
```

---

## 개발 환경

* Language : Python 3
* IDE : Visual Studio Code
* Version Control : Git & GitHub

---
