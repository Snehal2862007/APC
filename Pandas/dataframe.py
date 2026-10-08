import pandas as pd
students={"name":["a","b","c","d"],"marks":[10,20,12,13]}

marks=pd.DataFrame(students)
print(marks)
print(marks.index)
print(marks.columns)