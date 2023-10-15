import math
import timeit
import random

def collinearPoints(points):
    length = len(points)
    answer = []

    for z in range(length):
        v = points[z]
        slope = []
        # only_slope = []
        for i in range(0, length):
            if i != z:
                if (points[i][0] - v[0]) != 0:
                    temp_slope = (points[i][1] - v[1]) / (points[i][0] - v[0])
                    slope.append((points[i][0], points[i][1], math.floor(temp_slope * 1000000)/1000000))
                    # only_slope.append(math.floor(temp_slope))
                else:
                    temp_slope = float('inf')
                    slope.append((points[i][0], points[i][1], temp_slope))
                    # only_slope.append(temp_slope)

        slope = sorted(slope, key=lambda p:(p[2], p[0], p[1]))
        # slope.sort(key=lambda p:p[2])
        # only_slope.sort()

        
        # print(slope)
        # print(only_slope)

        cnt = 0
        slope_length = len(slope)
        samp = slope[0][2]
        # print(slope[0][2])

        for i in range(1, slope_length):
            if slope[i][2] != samp:
                if cnt >= 2:
                    back = i - 1
                    temp = [(points[z][0], points[z][1]), (slope[back][0], slope[back][1]), (slope[back - cnt][0], slope[back - cnt][1])]
                    temp.sort()
                    # print(temp)
                    b = (temp[0][0], temp[0][1], temp[2][0], temp[2][1])
                    # print(b)
                    if b not in answer:
                        answer.append(b)
                cnt = 0
                samp = slope[i][2]
            else:
                cnt += 1    # 기울기 같으면 추가 
                if (i == slope_length - 1) and (cnt >= 2):
                    temp = [(points[z][0], points[z][1]), (slope[i][0], slope[i][1]), (slope[i - cnt][0], slope[i - cnt][1])]
                    temp.sort()
                    # print(temp)
                    b = (temp[0][0], temp[0][1], temp[2][0], temp[2][1])
                    # print(b)
                    if b not in answer:
                        answer.append(b)
        
    answer.sort()
    return answer


def correctnessTest(input, expected_output, correct):
    output = collinearPoints(input)
    print(f"collinearPoints({input})\n{output}")
    if output == expected_output: print("Pass")
    else:        
        print(f"Fail - expected output: {expected_output}")
        correct = False
    print()    

    return correct


def simulateNSquareLogN(points):
    points = sorted(points, key=lambda p:(p[1], -p[0]))
    for i in range(0, len(points)):
        slopes = []
        for j in range(i+1, len(points)):
            if points[i][0] == points[j][0]: slopes.append((points[j][0], points[j][1], float('inf')))
            else: slopes.append((points[j][0], points[j][1], (points[j][1]-points[i][1])/(points[j][0]-points[i][0])))
        slopes.sort(key=lambda p:(p[1],p[2],p[0]))
        
        for j in range(1, len(slopes)):
            if slopes[j][2] == slopes[j-1][2]:
                for k in range(5): pass


'''
Unit Test
'''
if __name__ == "__main__":

    print("Correctness test for collinearPoints()")
    print("For each test case, if your answer does not appear within 5 seconds, then consider that you failed the case")
    print()
    correct = True

    # No collinear sets found, thus return the empty list []
    input = [(0,0),(1,1)]
    expected_output = []
    correct = correctnessTest(input, expected_output, correct)


    input = [(0,0), (1,1), (3,3), (4,4), (6,6), (7,7), (9,9)]
    expected_output = [(0,0,9,9)]    
    correct = correctnessTest(input, expected_output, correct)

    input = [(1,0), (2,0), (3,0), (4,0), (5,0), (6,0), (8,0)]
    expected_output = [(1,0,8,0)]
    correct = correctnessTest(input, expected_output, correct)

    input = [(7,0), (14,0), (22,0), (27,0), (31,0), (42,0)]
    expected_output = [(7,0,42,0)]
    correct = correctnessTest(input, expected_output, correct)

    input = [(0,0), (0,1), (0,2), (0,3), (0,4), (0,5), (0,-2), (0,-53)]
    expected_output = [(0, -53, 0, 5)]
    correct = correctnessTest(input, expected_output, correct)

    input = [(19000,10000), (18000,10000), (32000,10000), (21000,10000), (1234,5678), (14000,10000)]
    expected_output = [(14000,10000,32000,10000)]
    correct = correctnessTest(input, expected_output, correct)

    input = [(12446,18993), (12798,19345), (12834,19381), (12870,19417), (12906,19453), (12942,19489)]
    expected_output = [(12446,18993,12942,19489)]
    correct = correctnessTest(input, expected_output, correct)


    input = [(0,0), (0,1), (0,2), (0,3), (1,0), (1,1), (1,2), (1,3)]
    expected_output = [(0,0,0,3), (1,0,1,3)]
    correct = correctnessTest(input, expected_output, correct)

    input = [(10000,0), (0,10000), (3000,7000), (7000,3000), (20000,21000), (3000,4000), (14000,15000), (6000,7000)]
    expected_output = [(0, 10000, 10000, 0), (3000, 4000, 20000, 21000)]    
    correct = correctnessTest(input, expected_output, correct)    


    # Case where the same point appears multiple times
    input = [(1,1), (2,2), (3,3), (4,4), (2,0), (3,-1), (4,-2), (0,1), (-1,1), (-2,1), (-3,1), (2,1), (3,1), (4,1), (5,1)]
    expected_output = [(-3, 1, 5, 1), (1, 1, 4, -2), (1, 1, 4, 4)]
    correct = correctnessTest(input, expected_output, correct)    


    print()
    print("Speed test for collinearPoints()")
    if not correct: print("Fail (since the algorithm is not correct)")
    else:
        repeat = 10
        inputLength = 100
        minC, maxC = -1000000, 1000000
        points = [(random.randint(minC, maxC), random.randint(minC, maxC)) for _ in range(inputLength)]
        tCodeToCompare = timeit.timeit(lambda: simulateNSquareLogN(points), number=repeat) / repeat
        tSubmittedCode = timeit.timeit(lambda: collinearPoints(points), number=repeat) / repeat        
        print(f"Average running time of collinearPoints() and simulateNSquareLogN() with {inputLength} points: {tSubmittedCode:.10f} and {tCodeToCompare:.10f}")
        #print(f"{tSubmittedCode / tCodeToCompare}")
        if tSubmittedCode < tCodeToCompare * 3: print("Pass")
        else:
            print("Fail")
        print()
        
    