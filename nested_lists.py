"""
Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s)
of any student(s) having the second lowest grade.
Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each
name on a new line.
"""

if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])

    lowest = 101
    second_lowest = 101
    for record in records:
        if record[1] < lowest:
            second_lowest = lowest
            lowest = record[1]
        elif record[1] < second_lowest and record[1] != lowest:
            second_lowest = record[1]

    res = []
    for record in records:
        if record[1] == second_lowest:
            res.append(record[0])

    res = sorted(res)
    for i in res:
        print(i)
