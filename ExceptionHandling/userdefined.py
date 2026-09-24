class markerror(Exception):
    pass
marks = int(input("Enter marks: "))
try:
    if marks < 0 or marks > 100:
        raise markerror("Marks must be between 0 and 100.")
    else:
        print("Valid marks.")
except markerror as e:
    print("Exception:", e)