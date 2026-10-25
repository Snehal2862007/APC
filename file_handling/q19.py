import csv
rows = [["amit", 60, 80], ["priya", 75, 80], ["rahul", 55, 80]]
with open("attendance.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["name", "present", "total"])
    w.writerows(rows)
with open("attendance.csv", newline="") as f:
    for s in csv.DictReader(f):
        percent = int(s["present"]) / int(s["total"]) * 100
        print(s["name"], percent)
        if percent < 75:
            print("below 75%:", s["name"])
