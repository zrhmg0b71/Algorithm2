# Cycle Detection

## 1. Symbol Table
- 데이터(value)를 ID 역할하는 key와 함께 (key, value) 쌍으로 저장하는 데이터 구조 → key를 검색어로 사용해 대응되는 value를 빠르게 찾는 것
    - key : Unique
    - value : Unique할 필요 X, 어떤 객체도 value가 될 수 있음

### value에 리스트를 저장한 예
```python
stPokemon = {}  # Create an empty dictionary
# 빈 리스트 []와 다름!

# Insert (key, value) pairs
# 리자몽이 key, 볼꽃과 비행이 value
stPokemon["리자몽"] = ["불꽃", "비행"]
stPokemon["메가리자몽X"] = ["불꽃", "비행"]
stPokemon["메가리자몽Y"] = ["불꽃", "비행"]

# Given a key, find the corresponding value
print(stPokemon["메가리자몽X"])
# remove(x) : 리스트에서 원소 x를 삭제하는 함수
stPokemon["메가리자몽X"].remove("비행")
# append(x) : 리스트에 원소 x를 추가하는 함수
stPokemon["메가리자몽X"].append("드래곤")
print(stPokemon["메가리자몽X"])

# key k가 dictionary d에 포함되지 않았음 → k not in d 사용
# key k가 dictionary d에 포함되었음 → k in d
if "이상해꽃" not in stPokemon: stPokemon["이상해꽃"] = []
print(stPokemon["이상해꽃"])
types = stPokemon["이상해꽃"]
types.append("풀")
types.append("독")
print(stPokemon["이상해꽃"])
```

## 2. Set(집합) - Symbol Table을 변형한 자료구조
: Symbol table에서 value는 제거하고 key만 저장  
= 서로 다른 값을(서로 다른 key를) 원소로 저장하는 구조
- key의 존재 여부만 빠르게 확인 가능
- ex. Spell checker, Spam filter, Parental Controls

### spam words를 set에 저장한 예
```python
# 비어 있는 set 객체인 spamWords 생성
spamWords = set()
# set에 두 단어 추가 후 출력
spamWords.add("buy")
spamWords.add("promotion")
print(spamWords)

# update(x) : set에 리스트 x에 있는 모든 원소를 일괄적으로 추가
spamWords.update(["sale", "urgent", "warning", "thankyou"])
print(spamWords)

# remove(x) : set에서 원소 x를 삭제
spamWords.remove("thankyou")
print(spamWords)

if "urgent" in spamWords: print("urgent in spamWords")
else: print("urgent NOT in spamWords")
if "hope" not in spamWords: print("hope not in spamWords")
else: print("hope in spamWords")
```

### for loop를 사용해 set의 각 원소를 iterate
```python
for w in spamWords:
    print(w)

# 실행 결과
# urgent
# promotion
# buy
# warning
# sale
```
- set은 원소를 추가한 순서를 그대로 보존하는 자료 구조가 X      
→ 추가한 순서에 상관없이 원소가 집합에 속하는지 아닌지를 확인할 필요가 있을 때 사용
- 원소를 추가한 순서 필요 시
    - 별도의 리스트를 만들어 순서대로 저장하거나
    - set 대신 dictionary 사용해 원소를 key, 순서를 value로 저장해 사용

## 3. Digraph에 대한 기본 탐색 방법
### DFS
- 방법 : 출발지 s로부터 갈 수 있는 곳을 최대한 깊이까지 가본 후 왔던 길을 돌아 나오며 같은 방식으로 다른 길 탐색
- 특성
    - 출발지 s에서 도달 가능한 곳 모두 찾음
    - 임의 경로 찾음 & 최소 간선 경로 일수도 아닐수도
    - Topological order 항상 지키며 탐색
    - ~(V + E)
### BFS
- 방법 : 출발지 s에서 같은 거리에 갈 수 있는 모든 곳을 함께 병렬로 탐색
- 특성
    - 출발지 s에서 도달 가능한 곳 모두 찾음
    - 최소 간선 경로 찾음
    - Topological order 어길수도 있음
    - ~(V + E)
### Multi-source BFS
- 방법 : 둘 이상의 출발지 s에서 같은 거리에 갈 수 있는 모든 곳을 함께 병렬로 탐색
- 특성
    - 동시 출발지 여럿 → 같은 시간에 더 다양한 목적지 탐색 가능
    - 임의 경로 찾음 & 최소 간선 경로 일수도 아닐수도
    - ~(V + E)
