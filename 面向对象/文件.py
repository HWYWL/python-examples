# 文件读取
file_read = open("hello.txt", 'r', encoding='UTF-8')

text_read = file_read.read()
print(text_read)

file_read.close()

print("*" * 50 + "华丽分隔符" + "*" * 50)

# 文件写入
file_a = open("hello.txt", 'a', encoding='UTF-8')

file_a.write("我是写入。。。\r\n")

file_a.close()

print("*" * 50 + "华丽分隔符" + "*" * 50)

# 按行读取
file_read_line = open("hello.txt", 'r', encoding='UTF-8')
while True:
    test_line = file_read_line.readline()
    if not test_line:
        break

    print(test_line)

file_read_line.close()

print("*" * 50 + "华丽分隔符" + "*" * 50)

# 文件复制
file_only_read = open("hello.txt", 'r', encoding='UTF-8')
file_only_write = open("hello副本.txt", 'w', encoding='UTF-8')
while True:
    test_line = file_only_read.readline()
    if not test_line:
        break

    file_only_write.write(test_line)

file_only_read.close()
file_only_write.close()
