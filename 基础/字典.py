peri_dict = {
    "name": "小萝莉",
    "age": 18,
    "sex": "女"
}
print(peri_dict)

print(peri_dict.get("name"))

# 获取所有key
print(peri_dict.keys())
# 获取所有value
print(peri_dict.values())
# 获取所有key和value
print(peri_dict.items())

for key in peri_dict:
    print("%s : %s" % (key, peri_dict[key]))
