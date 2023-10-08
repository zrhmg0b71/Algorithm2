# Selection Sort
: 매 iteration마다 입력 데이터의 일부 중에서 가장 작은 원소를 선정해(selection) 앞으로 이동시키는 정렬 방식

## 1. 수행 방법
- 정렬할 데이터 N개가 배열 a[]에 저장되어 있으며 오름차순으로 정렬한다고 할 때,
- 0 ~ (N - 1)까지 loop를 돌면서 a[]의 일부에 대해 가장 작은 원소를 찾아 가장 왼쪽으로 보내는 것을 반복
- Iteration i 때 a[i] ~ a[N - 1] 중 가장 작은 원소 찾아 a[i]와 위치 바꿈 (swawp)
- 가장 작은 원소 찾기 위해 a[i] ~ a[N - 1] 하나씩 차례로 확인함

## 2. Code
```python
def selectionSort(a):
    for i in range(len(a) - 1):     # 0 ~ (N - 2)까지 loop
        # Find the minimum in a[i] ~ a[N - 1]
        min_idx = i
        for j in range(i + 1, len(a)):
            if a[j] < a[min_idx]:
                min_idx = j     # 최솟값의 인덱스 저장 

        # Swap the found minimum with a[i]
        a[i], a[min_idx] = a[min_idx], a[i]
```

## 3. 성능 분석
(1) 두 원소 간 대소 비교, (2) 위치 바꾸기 (swap)

### 비교 횟수
: iteration i에서는 a[i]를 a[i + 1] ~ a[N - 1]과 차례로 비교    
→ (N - 1) - (i + 1) + 1 = N - 1 - i 회의 비교   
→ i = 0 ~ N - 2 까지 진행   
→ 총 비교 횟수 : (N - 1) + (N - 2) + ... + 1 = (N - 1)N / 2 = ~N^2 / 2

### Swap 횟수
: 매 iteration 마다 최솟값을 찾은 후 이 값을 a[i]와 swap    
→ N에 비례한 횟수의 swap 수행
- 입력 데이터가 달라도 변함 X
    - 거의 정렬이 다 된 상태로 들어와도 전체를 다 비교하기 때문

---
# Insertion Sort
: 매 iteration마다 정렬된 상태인 a[0] ~ a[i - 1]에 새로운 한 원소 a[i]를 적절한 위치에 추가하는 (insert) 정렬 방식

## 1. 수행 방법 
- 정렬할 데이터 N개가 배열 a[]에 저장되어 있으며 오름차순으로 정렬한다고 할 때,
- Iteration i 때 a[i]를 왼쪽의 원소와 swap 하는 데, 그보다 크지 않은 원소가 나오기 직전까지 swap

## 2. Code
```python
def insertionSort(a):
    for i in range(1, len(a)):     # 1 ~ (N - 1)까지 loop
        key = a[i]      # Element to move at current iteration

        j = i - 1       # 한 칸 앞
        while j >= 0 and a[j] > key:
            # Move element a[j] to a[j + 1] if a[j] > key
            a[j + 1] = a[j]
            j -= 1

        # Place the key to the farthest it can go to the left
        a[j + 1] = key
```

## 3. 성능 분석
: 인접한 원소끼리 swap 하므로 Inversion 수만큼 비교 & swap 수행

### Inversion
: 정렬 순서가 어긋난 쌍
- Inversion이 없으면 정렬된 상태 

### 비교 횟수
- best case → 입력 데이터 a[]가 이미 정렬된 상태로 들어올 때 : N - 1 → ~N
- worst case → 반대 방향으로 정렬된 상태 : 1 + 2 + ... + (N - 1) = (N - 1)N / 2 → ~N^2/2
- average case → 각 원소를 절반 정도 이동시켜야 하는 상태 : worst case / 2 → ~N^2 / 4

### Swap 횟수
- best case → 입력 데이터 a[]가 이미 정렬된 상태로 들어올 때 : 0
- worst case → 반대 방향으로 정렬된 상태 : 1 + 2 + ... + (N - 1) = (N - 1)N / 2 → ~N^2/2
- average case → 각 원소를 절반 정도 이동시켜야 하는 상태 : worst case / 2 → ~N^2 / 4

### 정리
- 순서를 바꾸어야 할 원소 쌍이 N에 비례한 개수 이하라면 ~N회 작업이 필요한 Insertion Sort가 다른 Sorting 보다 유리함 → Partially ordered 된 상태

# 임의의 데이터 타입 정렬 시 유의 사항
- 대소 관계가 명확하지 않은 객체 정렬 시 대소 관계 비교에 필요한 대소 관계를 규칙에 따라 잘 정의해야 함
## 대소 관계 정의 시 지켜야 할 규칙 (Total Order)
- Anti-symmetry : if a <= b and b <= a, then a == b
- Transitivity : if a <= b and b <= c, then a <= c
- Totality : for every pair of elements a and b, either a < b or a > b or a==b
- 세 가지 규칙 다 지키도록 원소 간의 대소 관계 정의한 경우 : total order를 만족함 

---
# h-sort
: 모든 h만큼 떨어진 원소끼리 (insertion sort 방식으로) 정렬된 상태로 만듦 → 한 칸 떨어진 원소 간에는 모두 정렬되지 않음 
: Shell sort의 기본 operation

1. 수행 방법
: Insertion sort를 h칸 간격으로 수행 

## 2. Code
```python
def hInsertionSort(a, h):
    for i in range(h, len(a)):  # a[h]부터 왼쪽으로 이동시킴
        key = a[i]
        j = i - h
        while j >= 0 and a[j] > key:
            a[j + h] = a[j]
            j -= h      # h칸 씩 왼쪽으로 이동하며 비교 & swap
        a[j + h] = key
```
- Insertion Sort와 다른 점은 1 대신 h를 썼다는 것밖에 없음!
---
# Shell Sort
: h를 점진적으로 1까지 감소시켜 가며 h-sort 수행
: h는 1씩 감소시키지 않고 그보다 큰 간격으로 감소

1. Insertion Sort보다 대체로 빠른 이유
: 여러 차례 비교와 swap을 통해 여러 칸 앞으로 가야할 것들을 한 번에 h칸씩 앞으로 이동시켜 비교하고 swap 횟수를 줄이기 때문 → 한 swap으로 여러 inversion 한 번에 해결

