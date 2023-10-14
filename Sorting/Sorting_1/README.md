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
→ 총 비교 횟수 : (N - 1) + (N - 2) + ... + 1 = (N - 1)N / 2 = ~N<sup>2</sup> / 2

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
- worst case → 반대 방향으로 정렬된 상태 : 1 + 2 + ... + (N - 1) = (N - 1)N / 2 → ~N<sup>2</sup>/2
- average case → 각 원소를 절반 정도 이동시켜야 하는 상태 : worst case / 2 → ~N<sup>2</sup> / 4

### Swap 횟수
- best case → 입력 데이터 a[]가 이미 정렬된 상태로 들어올 때 : 0
- worst case → 반대 방향으로 정렬된 상태 : 1 + 2 + ... + (N - 1) = (N - 1)N / 2 → ~N<sup>2</sup> /2
- average case → 각 원소를 절반 정도 이동시켜야 하는 상태 : worst case / 2 → ~N<sup>2</sup> / 4

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

## 1. 수행 방법
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
: h는 1씩 감소시키지 않고 그보다 큰 간격으로 감소 → 최종적으로 1-sort 수행해 완전히 정렬된 상태로 만듦

## 1. Insertion Sort보다 대체로 빠른 이유 (비교 & Swap 횟수 줄어드는 이유)
: 여러 차례 비교와 swap을 통해 여러 칸 앞으로 가야할 것들을 한 번에 h칸씩 앞으로 이동시켜 비교하고 swap 횟수를 줄이기 때문 → 한 swap으로 여러 inversion 한 번에 해결

## 2. 여러번의 h-sort해도 괜찮은 이유 (각 h-sort가 Insertion Sort(~N^2)만큼 오래 걸리지 않는 이유)
: 여러 칸 (h > 1) 떨어진 원소끼리만 비교해서 비교 & swap 횟수 적음
: h = 1일 때 Insertion Sort와 같지만 이전의 h-sort들에 의해 거의 정렬된 상태이므로 (Inversion 수가 ~N에 가까이 줄어든 상태) ~N에 가까운 비교 & swap만으로 완료

## 3. h-sort으ㅣ h 값 선정 방법
- 조건 : h를 어떤 방식으로 선택하더라도 최종적으로 h = 1 해서 완전히 정렬된 상태로 만들어야 함.
- Donald Knuth 방법 : k = 3x + 1    (계산이 쉬움 + 성능↑ ⇒ 가장 많이 사용)

## 4. Shell Sort의 성능
- h = 3x + 1 사용 시 ~logN회의 h-sort 수행 ⇒ ~NlogN의 비교 / Swap 수행할 것으로 예측됨 (아직 정확한 수학적 모델이 없어 예측)

---
# Shuffle Sort

## 1. 개념
- shuffle : 입력 데이터의 순서를 임의로 섞음 (uniformly random하게 섞으면 N!가지 경우 나옴)

## 2. shuffling 방법
- 모든 가능한 permutation 발생시킨 후 하나 선정 (N!개의 경우 만들어야 함 → 매우 비효율적)
- sort를 직접 활용 (shuffle sort) : 입력 데이터의 각 원소에 대해 random 실수 발생 (~N) → 발생한 실수 값을 key로 사용해 정렬 (~NlogN) ⇒ ~NlogN
    - uniformly random 분포로부터 난수 발생시키면 shuffle 결과도 uniformly random함

## 3. Code
```python
import random

def shuffleSOrt(a):
    # Generate a random real number for each entry in a[]
    r = []
    # (1) 입력 데이터 a의 길이만큼 난수 발생
    for _ in range(len(a)):
        r.append(random.random())

    # Sort according to the random real number
    # (2) a의 각 원소와 난수를 tuple로 결합
    # (3) 발생시킨 난수를 key로 사용해 정렬
    # (4) 정렬 결과에서 난수는 제거하고 원래 a에 속한 원소만 반환
    return [i for i, _ in sorted(zip(a, r), key = lambda x: x[1])]
```

## 4. Knuth's Shuffle
: Iteration i 때 a[0] ~ a[i] 중 하나를 uniformly random하게 선정해 a[i]와 swap
→ a[0] ~ a[i]가 uniformly random하게 shuffle된 상태가 됨.

### 성능 비교
- 각 iteration에서의 비교 횟수 : 1번
- 각 iteration에서의 swap 횟수 : 1번
- 즉, 각 iteration이 상수 시간이 걸리기 때문에 ~N

### Code
```python
import random

def knuthShuffle(a):
    for i in range(1, len(a)):
        j = random.randint(0,i) # Randomly select a position among 0 ~ i
        a[i], a[j] = a[j], a[i] # Swap a[i], a[j]

    return a
```

---
# Convex Hull
: N개 정점 전체 혹은 일부를 사용해 만들 수 있는 다각형 중 정점 모두를 내부에 포함하면서 최소 정점으로 만들 수 있는 다각형

## 1. 성질
- 반시계 방향 순서로 선택 = 최저점과 각도 순으로 선택
- 모든 정점은 볼록한 각을 만들어야 함 (오목한 각은 하나도 존재 X)


## 2. 활용 예시
- Robot Motion Planning : Polygon(다각형) 형태 장애물 있을 때 두 지점 s와 t 간 최단 경로 찾기
- Farthest Pair 찾기 : 평면 상에 N개의 점이 있을 때, 서로 거리가 가장 먼 두 점 찾기

## 3. 찾는 방법
### 0> N개 점에 대한 모든 가능한 부분집합 찾아 다른 점들 포함하는지 검사 : ~2<sup>N</sup>
### 1> 반시계 방향의 turn을 반복하며 각 점을 따라감
- (1) y값이 가장 작은 점을 시작점으로 선정
    - y가 같으면 x값이 가장 큰 점
    - y값이 가장 작은 점을 시작점으로 선정하는 이유 : 반시계 방향 순서로 선택하기 때문에. y값이 가장 작은 점으로부터의 각도가 증가하는 순으로 선택하면 convex hull을 반시계 방향으로 따라 가는 순서가 됨.
- (2) 좌향좌를 가장 작은 각도로 하면 되는 정점을 다음 정점으로 선택
### 2> Graham's Scan
: 최저점으로부터 반시계방향 각도 순 연결 → concave angle 만드는 점 제외 
- y값 가장 작은 점 p에서 시작해 다른 모든 점과의 반시계 방향 각도 계산해서 정렬
- 각도가 작은 점 순으로 차례로 연결해보면서 새로운 점 연결할 때마다 아래 수행
    - 마지막에 i → j → k 순으로 연결했으면 i-j선 기준 j-k가 반시계방향의 turn이 아니면(즉 concave angle 발생 시) j는 convex hull에서 제외 ⇒ i-k 직접 연결
    - 더 이상 제외할 점 없을 때까지 마지막 세 점의 concave 여부 확인 반복
- 더 연결할 점 없으면 제외 안했던 모든 점들 순서대로 연결하면 convex hull됨

## 4. 성능 분석
### 1번 방법의 성능>
- 시작점 선정 : ~N
- 다음 점 선정 : (N - 1) + (N - 2) + (N - 3) + ... + 1 = ~N<sup>2</sup>
### 2번 방법의 성능>
- 시적점 p 찾기 : ~N
- p와 다른 점 간 각도 계산 : ~N
- 각도에 따라 정렬 : ~NlogN
- 새로운 점 포함 : ~N
- 볼록 검사 fail → 점 삭제 : ~N
- 볼록 검사 pass : ~N

## 5. 공식
- convex angle 확인 방법 (오목/볼록 검사 식) : 2 * 면적(i, j, k)
= (j<sub>x</sub> - i<sub>x</sub>)(k<sub>y</sub> - i<sub>y</sub>) - (j<sub>y</sub> - i<sub>y</sub>)(k<sub>x</sub> - i<sub>x</sub>)
    - <= 0 이면 j 제거 후 Fail

## 6. Code
```python
# Determine if the line i->j->k is a counter-clockwise turn
# Each of i, j, and k is a 2-tuple (x coordinate, y coordinate)
# 오목 / 볼록 검사 식 
def ccw(i, j, k):
    area2 = (j[0] - i[0]) * (k[1] - i[1]) - (j[1] - i[1]) * (k[0] - i[0])
    if area2 > 0: return True
    else: return False

if __name__ == "__main__":
    # ccw turns
    print(ccw((0, 0), (-1, 1), (-2, -1)))

    # non-ccw turns
    print(ccw((0, 0), (-2, -1), (-1, 1)))
    print(ccw((0, 0), (-1, 1), (-2, 2)))  # Straight line
```