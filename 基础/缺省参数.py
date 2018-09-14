# 必须保证带有默认参数的缺省参数在参数列表最后面
def user_info(name, gender=True):
    gender_text = "男生"

    if not gender:
        gender_text = "女生"

    print("%s 是 %s " % (name, gender_text))
    

user_info("小明")
user_info("小妹", False)