'''
Class that represents a stack
'''
class Stack:
    def __init__(self): # Constructor        
        # Stack 클래스 생성자
        # 멤버 변수 self.list를 빈 리스트로 초기화
        # 아래와 같이 작성
        self.list = []

    def push(self,x): # Add to the end
        # Stack 가장 뒤에 x를 추가
        # 아래와 같이 작성
        self.list.append(x)

    def pop(self): # Return the last item   
        # stack 이 비어있을 경우            
        if not self.list: return None
        # stack 안에 원소가 있을 경우
        else:
            return self.list.pop()


def correctnessTest(input, expected_output, correct):
    print(f"input:{input}")
    s = Stack()
    for e in input: s.push(e)
    result = []
    for _ in range(len(expected_output)): result.append(s.pop())
    print(f"output:{result}")
    if result == expected_output: print("Pass")
    else: 
        print(f"Fail: output is not equal to the expected output {expected_output}")
        correct = False
    print()

    return correct


if __name__ == "__main__": 
    '''
    Unit Test
    '''    
    print("Correctness test for class Stack")
    print("For each test case, if your answer does not appear within 5 seconds, then consider that you failed the case")
    print()
    correct = True
    
    input, expected_output = [], [None, None]
    correct = correctnessTest(input, expected_output, correct)

    input, expected_output = [1, 2, 3, 4], [4, 3, 2, 1, None, None]
    correct = correctnessTest(input, expected_output, correct)
    
    input, expected_output = [-25, 4, 100, 72, -11, 16], [16, -11, 72, 100, 4, -25, None, None, None, None, None, None, None]
    correct = correctnessTest(input, expected_output, correct)
