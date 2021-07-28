def solution(answers):
    answer = []
    person1 = [1, 2, 3, 4, 5]
    person2 = [2, 1, 2, 3, 2, 4, 2, 5]
    person3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    count = {1:0, 2:0, 3:0}
    
    for i in range(len(answers)):
        if answers[i] == person1[i % len(person1)]:
            count[1] += 1
        if answers[i] == person2[i % len(person2)]:
            count[2] += 1
        if answers[i] == person3[i % len(person3)]:
            count[3] += 1
    grade = sorted(count.items(), key=lambda x: x[1], reverse=True)
    first = grade[0][0]
    answer.append(first)
    if grade[0][1] == grade[1][1]:
        answer.append(grade[1][0])
    if grade[0][1] == grade[2][1]:
        answer.append(grade[2][0])

    return answer
