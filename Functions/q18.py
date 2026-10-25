def result(marks):
    per = sum(marks) / 5
    if per >= 75:
        grade = "a"
    elif per >= 60:
        grade = "b"
    elif per >= 40:
        grade = "c"
    else:
        grade = "fail"
    return per, grade

print(result([80, 75, 90, 85, 70]))