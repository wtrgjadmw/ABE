import re

re_str = r"\d{1,2}"
str = "MAIN_MEM_R10"
m = re.search(re_str, str)
print(m.group())
print(str[:m.start()])