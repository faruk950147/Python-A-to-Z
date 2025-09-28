def find_second_lowest_students(students):
    grades = sorted(set([grade for name, grade in students]))
    second_lowest = grades[1]
    result = sorted([name for name, grade in students if grade == second_lowest])
    return result

if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        grade = float(input())
        students.append([name, grade])

    for name in find_second_lowest_students(students):
        print(name)

  
if __name__ == "__main__":
    students = []
    for _ in range(int(input())):
        name = input()
        grade = float(input())
        students.append([name, grade])

    grades = sorted(set([grade for name, grade in students]))
    second_lowest = grades[1]
    result = sorted([name for name, grade in students if grade == second_lowest])
    # if we needs defrent sort
    # result = [name for name, grade in students if grade == second_lowest]
    # result.sort()
    for name in result:
        print(name)
