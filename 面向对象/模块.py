def say_hello():
    print("Hello Python")


# 只有本方法中才会执行，导入到其他模块不执行
if __name__ == "__main__":
    print("Hello 嘿嘿嘿")
    say_hello()