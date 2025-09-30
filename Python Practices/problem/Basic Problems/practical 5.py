def grade_calculator(marks):    
    if marks >= 90:
        print("Grade A")
    elif marks >= 80:
        print("Grade B")
    elif marks >= 70:
        print("Grade C")
    elif marks >= 60:
        print("Grade D")
    else:
        print("Grade F")    

grade_calculator(95)


def grade_calculator_with_percentage(marks):   
    percentage = (marks / 100) * 100
    if percentage >= 90:
        print("Grade A")
    elif percentage >= 80:
        print("Grade B")
    elif percentage >= 70:
        print("Grade C")
    elif percentage >= 60:
        print("Grade D")
    else:
        print("Grade F")

grade_calculator_with_percentage(95)