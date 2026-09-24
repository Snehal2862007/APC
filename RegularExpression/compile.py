#findall and compile
# import re
# pattern = re.compile("\d+")
# a ="I have 25 apples and 10 bananas."
# result = pattern.findall(a)
# print(result)

# search
# import re
# text = "i am learning python"
# result = re.search("python", text)
# print(result.group())

# substitute
# import re
# text="i am happy"
# result=re.sub("happy","sad",text)
# print(result)

# split
import re
text="apple1 orange1banana"
result=re.split("1",text)
print(result)