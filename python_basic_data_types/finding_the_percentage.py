'''
dict stores students in format:
    { 'name': [score,score,score],...}
where name is string and score is integer.

goal: select a name and return the average of scores to 2dp
'''
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    print("%.2f" % round(sum(student_marks[query_name]) / 3, 2))
