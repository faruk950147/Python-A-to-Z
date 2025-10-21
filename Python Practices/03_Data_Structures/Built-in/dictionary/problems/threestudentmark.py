faruk = {"C": 80, "C++": 90, "C#": 70}
tamim = {"Python": 80, "Java": 90, "JS": 70}
tonmoy = {"HTML": 80, "CSS": 90, "Bootstrap": 70}
students = [faruk, tamim, tonmoy]
for student in students:
    sum1 = 0
    for item in student:
        sum1 += student[item]
    print(sum1)