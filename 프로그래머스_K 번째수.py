# problem
# 배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 수를 구하려 합니다.


# My answer
def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        answer.append(array[commands[i][0] - 1 : commands[i][1]])
    for i in range(len(commands)):
        answer[i] = sorted(answer[i])
        answer[i] = answer[i][commands[i][2] - 1]
    
    return answer
  
# result
#정확성: 100.0
#합계: 100.0 / 100.0
