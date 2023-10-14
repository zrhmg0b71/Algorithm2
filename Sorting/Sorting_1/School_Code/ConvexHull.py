import math
import timeit
import random

# Given a list of points (x, y)
#   find the convex hull using Graham's Scan
# Return a list of points in the convex hull in ccw order
def grahamScan(points):
    # p점 찾기 : y값이 가장 작은 점 중 x값이 가장 큰 점
    find_p_points = sorted(points, key = lambda p: (p[1], -p[0]))
    p = find_p_points[0]

    # 각도 계산해서 리스트에 정렬
    length = len(points)
    ang_list = []
    # ang_list 속 튜플 : (x 좌표, y 좌표, p와의 각도)
    # p의 x 좌표, y 좌표, 0을 list의 첫 인덱스로 삽입
    ang_list.append((find_p_points[0][0], find_p_points[0][1], 0))
    # 나머지 점들도 넣기
    # math.atan2는 arc tangent. 즉 tangent 역함수를 의미. 반환값은 -180 ~ +180 사이
    # math.atan2(ay - py, ax - px)
    for i in range(1, length):
        ang_list.append((find_p_points[i][0], find_p_points[i][1], math.atan2(find_p_points[i][1] - p[1], find_p_points[i][0] - p[0])))
    # 각도 순서대로 정렬
    ang_sorted_list = sorted(ang_list, key = lambda p: (p[2]))

    # 하나씩 넣어보며 확인
    result = []
    result.append(p)    # p는 무조건 convex hull에 포함되기 때문
    result.append((ang_sorted_list[1][0], ang_sorted_list[1][1]))

    for i in range(2, length):
        result.append((ang_sorted_list[i][0], ang_sorted_list[i][1]))
        while True:
            if len(result) < 3:
                break
            # 리스트에 담긴 것 중 맨 마지막 3개를 ccw 함수에 넣고 오목/볼록 검사
            ans = ccw(result[-3], result[-2], result[-1])
            if ans == True:
                break
            else: 
                result.pop(-2)

    return result

def ccw(i, j, k):
    area2 = (j[0] - i[0]) * (k[1] - i[1]) - (j[1] - i[1]) * (k[0] - i[0])
    if area2 > 0: return True
    else: return False


def correctnessTest(intput, expected_output, correct):
    output = grahamScan(input)
    print(f"grahamScan({input})\n{output}")
    if output == expected_output: print("Pass")
    else:        
        print(f"Fail - expected output: {expected_output}")
        correct = False
    print()    

    return correct


def simulateNSquare(points):    
    points = sorted(points, key = lambda p: (p[1], -p[0])) 
    result = []
    for i in range(len(points)):
        points_with_angle = []
        for j in range(i+1, len(points)):
            x, y = points[j]
            points_with_angle.append((x, y, math.atan2(y - points[i][1], x - points[i][0])))
        points_with_angle = sorted(points_with_angle, key = lambda p: p[2])


'''
Unit Test
'''
if __name__ == "__main__":
    '''# ccw turns
    print(ccw((0,0), (-1,1), (-2, -1)))
    print(ccw((-1,1), (-2, -1), (0,0)))
    print(ccw((-2, -1), (0,0), (-1,1)))

    # non-ccw turns
    print(ccw((0,0), (-2, -1), (-1,1)))
    print(ccw((-2, -1), (-1,1), (0,0)))
    print(ccw((-1,1), (0,0), (-2, -1)))
    print(ccw((0,0), (-1, 1), (-2, 2))) # Straight line'''

    print("Correctness test for grahamScan()")
    print("For each test case, if your answer does not appear within 5 seconds, then consider that you failed the case")
    print()
    correct = True
    
    input = [(3, -1), (2, -2), (4, -1)]
    expected_output = [(2, -2), (4, -1), (3, -1)]
    correct = correctnessTest(input, expected_output, correct)

    input = [(0, 0), (-2, -1), (-1, 1), (1, -1), (3, -1), (-3, -1)]
    expected_output = [(3, -1), (-1, 1), (-3, -1)]
    correct = correctnessTest(input, expected_output, correct)

    input = [(4, 2), (3, -1), (2, -2), (1, 0), (0, 2), (0, -2), (-1, 1), (-2, -1), (-2, -3), (-3, 3), (-4, 0), (-4, -2), (-4, -4)]
    expected_output = [(-4, -4), (2, -2), (3, -1), (4, 2), (-3, 3), (-4, 0)]
    correct = correctnessTest(input, expected_output, correct)

    input = [(2, 0), (2, 2), (1, -1), (0, 2), (-1, 1), (-2, -2)]
    expected_output = [(-2, -2), (1, -1), (2, 0), (2, 2), (0, 2), (-1, 1)]
    correct = correctnessTest(input, expected_output, correct)

    input = [(2, 0), (2, 2), (1, -1), (0, 2), (-1, 1), (-2, -2), (-2, 2), (4, -4)]
    expected_output = [(4, -4), (2, 2), (-2, 2), (-2, -2)]
    correct = correctnessTest(input, expected_output, correct)

    # "342235" is a 6-digit number and is greater than the other 5-digit numbers
    input = [(342235, -23412), (-74545, 72345), (25812, -45689), (-45676, 24578), (45689, 0), (-74545, 0), (0, 45689), (0, -45689)]
    expected_output = [(25812, -45689), (342235, -23412), (-74545, 72345), (-74545, 0), (0, -45689)]
    correct = correctnessTest(input, expected_output, correct)
    
    print()
    print("Speed test for grahamScan()")
    if not correct: print("Fail (since the algorithm is not correct)")
    else:
        repeat = 10
        inputLength = 100
        minC, maxC = -1000000, 1000000
        points = [(random.randint(minC, maxC), random.randint(minC, maxC)) for _ in range(inputLength)]
        tSubmittedCode = timeit.timeit(lambda: grahamScan(points), number=repeat) / repeat
        tCodeToCompare = timeit.timeit(lambda: simulateNSquare(points), number=repeat) / repeat
        print(f"Average running time of grahamScan() and simulateNSquare() with {inputLength} points: {tSubmittedCode:.10f} and {tCodeToCompare:.10f}")                
        if tSubmittedCode < tCodeToCompare * 0.1: print("Pass")
        else:
            print("Fail")
        print()