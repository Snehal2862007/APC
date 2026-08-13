import re
from datetime import datetime

text = input("enter text: ")

pattern = r'\d{2}/\d{2}/\d{4}|\d{2}-\d{2}-\d{4}|\d{4}\.\d{2}\.\d{2}|[a-zA-Z]+ \d{1,2}, \d{4}'

dates = re.findall(pattern, text)

for date in dates:
    if "/" in date:
        d = datetime.strptime(date, "%d/%m/%Y")
    elif "-" in date:
        d = datetime.strptime(date, "%m-%d-%Y")
    elif "." in date:
        d = datetime.strptime(date, "%Y.%m.%d")
    else:
        d = datetime.strptime(date, "%B %d, %Y")

    print(d.strftime("%Y-%m-%d"))