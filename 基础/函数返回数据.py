def test():
    temp = 10
    wetness = 30

    return temp, wetness


# 函数调用
gl_temp, gl_wetness = test()
print(gl_temp)
print(gl_wetness)


def test1():
    name_list = ["校花", "小萝莉", "美女", "御姐"]

    return name_list


gl_name_list = test1()
print(gl_name_list)


def test2():
    student_dict = {"name": "小萝莉", "age": 18, "sex": "妹子"}

    return student_dict


gl_student_dict = test2()
print(gl_student_dict)
