# Python 词频统计
with open('a.txt', 'r') as f:
    str = f.read()
str = str.replace(",", " ")
str = str.replace(".", " ")
str = str.replace("!", " ")
str = str.replace("?", " ")
str = str.replace(":", " ")
str = str.replace(";", " ")
str = str.replace("\'", " ")
str = str.replace("/", " ")
str_list = str.split()
str_dict = {}
for i in str_list:
    if i in str_dict.keys():
        str_dict[i] = int(str_dict[i]) + 1
    else:
        str_dict[i] = 1
result = sorted(str_dict.items(), key=lambda e:e[1])
print(result.pop())
print(result.pop())
print(result.pop())