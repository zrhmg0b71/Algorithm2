# Indexed minPQ

## 1. minPQ VS Indexed minPQ
- key : PQ에 원소 저장 시 이들 간 우선 순위를 결정하는 값
- Indexed PQ : PQ에 저장한 원소의 key 값을 변경하는 기능을 추가한 PQ
    - PQ에 저장된 원소 e의 key를 변경하려면 **e를 다른 원소와 구분할 수 있는 ID(index)**가 필요
        - 동일한 key를 가진 원소들이 있을 수 있고, key는 변경할 수 있기 때문
### minPQ
- minPQ() : minPQ 객체 생성
- insert(key) : key를 PQ에 추가
- delMin() : key 가장 작은 원소 반환
- size() : PQ에 저장된 원소 개수 반환
### Indexed minPQ
- IndexMinPQ(**N**) : **index 0 ~ (N - 1)까지 사용 가능**한 minPQ 생성
    - minPQ 생성 시 미리 index 범위 지정하는 이유 : 범위에 맞게 index와 key 간 대응 관계를 저장할 배열을 마련하기 때문
- insert(**i**, key) : key를 **index i와 함께** PQ에 저장
- delMin() : key 가장 작은 원소 반환
- size() : PQ에 저장된 원소 개수 반환
- **contains(i) : index i를 PQ에 저장된 원소가 사용 중인가?**
- **decreaseKey(i, key) : index i 사용하는 원소의 key를 key로 감소**
    - 감소만 되는 것은 아니고 증가(increaseKey), 증가/감소 모두(changeKey)도 가능
- **keyOf(i) : index i 사용하는 원소의 key 반환**

## 2. 성능 비교
### minPQ
- insert(key) : ~logN
- delMin() : ~logN
### Indexed minPQ
- insert(**i**, key) : ~logN
    - heap 가장 끝에 추가한 후 swim up 과정 거침
- delMin() : ~logN
    - root 삭제 후 heap 가장 끝에 있던 원소 e를 root 자리에 배치 후 sink 과정 거침
- **decreaseKey(i, key)** : ~logN
    - a. heap에서 e가 어디에 있는지 탐색 → 배열에 저장돼있음 → ~1
    - b. 찾은 원소의 key 변경 → ~1
    - c. root 방향으로 올ㄹ라갈 수 있는 지점까지 swim up → ~logN

---
# Weighted Undirected Graph (WUGraph)
: 간선에 weight(비중, 비용)이 있으면서 방향성은 없는 그래프

## 1. WUGraph
- 그래프의 간선을 특징짓는 값에 따라 구분할 필요가 있을 때 weight 사용
- weight 사용 시 임의의 두 지점을 연결하는 최단 경로 선정 가능

## 2. Code
```python
class Edge:
    # Edge 객체의 생성자 
    def __init__(self, v, w, weight):  
        # 간선 출력 시 index가 증가하는 순서로 출력하기 위해
        if v <= w: self.v, self.w = v, w
        else: self.v, self.w = w, v
        self.weight = weight

    # 두 Edge 객체의 대소 비교 : 적절한 위치로 이동 혹은 정렬 시 사용
    def __lt__(self, other):  # < operator, used to sort elements
        assert(isinstance(other, Edge))
        return self.weight < other.weight

    # 두 Edge 객체의 대소 비교 : 적절한 위치로 이동 혹은 정렬 시 사용
    def __gt__(self, other):  # > operator, used to sort elements
        assert(isinstance(other, Edge))
        return self.weight < other.weight

    # Edge 객체 출력 : 디버깅에 사용
    def __str__(self):  # Called when an Edge instance is printed
        return f"{self.v} - {self.w} ({self.weight})"
    
    # Edge 객체의 정점 하나를 입력으로 받아 다른 정점을 반환
    def other(self, v):  # Return the vertex other than v
        if self.v == v: return self.w
        else: return self.v

# 그래프의 간선을 Edge 클래스의 객체로 나타냄
class WUGraph:
    def __init__(self, V):  # 생성자
        self.V = V  # Number of vertices
        self.E = 0  # Number of edges
        self.adj = [[] for _ in range(V)]  # adj[v] : v에 인접한 간선 목록
        self.edges = []  # WUGraph에 속한 모든 간선 저장

    # WUGraph 객체에 새로운 간선 추가
    def addEdge(self, v, w, weight):
        # 새로운 Edge 객체 생성
        e = Edge(v, w, weight)
        self.adj[v].append(e)
        self.adj[w].append(e)
        self.edges.append(e)
        self.E += 1

    # 그래프 출력 시 사용
    def __str__(self):
        rtList = [f"{self.V} vertices and {self.E} edges\n"]
        for v in range(self.V):
            for e in self.adj[v]:
                if v == e.v: rtList.append(f"{e}\n") # Do not print the same edge twice
        return "".join(rtList)
    
    # 파일에서 그래프 정보 읽어와 이로부터 WUGraph 그래프 객체 만들어 반환
    def fromFile(fileName):
        filePath = Path(__file__).with_name(fileName)   # Use the location of the current .py file   
        with filePath.open('r') as f:
            phase = 0
            line = f.readline().strip() # Read a line, while removing preceding and trailing whitespaces
            while line:                                
                if len(line) > 0:
                    if phase == 0: # Read V, the number of vertices
                        g = WUGraph(int(line))
                        phase = 1
                    elif phase == 1: # Read edges
                        edge = line.split()
                        if len(edge) != 3: raise Exception(f"Invalid edge format found in {line}")
                        g.addEdge(int(edge[0]), int(edge[1]), float(edge[2]))                        
                line = f.readline().strip()
        return g
```

---
# Union Find
: 연결 상태 변경 & 확인

## 1. 정의
N개의 정점이 주어졌을 때, vertex는 0 ~ (N - 1), edge는 없는 상태로 싲작
- Union(a, b) : 점 a와 b를 간선으로 연결
- Connected(a, b) : a와 b 연결하는 경로 존재하는지 True/False로 응답
    - connected component를 확인하는 것
    - 각 정점이 속한 connected component의 ID를 기록하는 배열 ids[]를 통해 ID가 같으면 True, 다르면 False 반환

## 2. Code
```python
class UF:
    def __init__(self, V):  # V : the number of vertices
        self.ids = []  # ids[i] : i's parent
        self.size = []  # size[i] : size of tree rooted at i
        for idx in range(V):
            self.ids.append(idx)
            self.size.append(1)
    
    def root(self, i):
        while i != self.ids[i]: i = self.ids[i]
        return i

    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def union(self, p, q):
        id1, id2 = self.root(p), self.root(q)
        if id1 == id2: return
        if self.size[id1] <= self.size[id2]:
            self.ids[id1] = id2
            self.size[id2] += self.size[id1]
        else:
            self.ids[id2] = id1
            self.size[id1] += self.size[id2]
```