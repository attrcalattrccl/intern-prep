try:
    num = int(input("请输入一个数字："))
    print(10 / num)
except ValueError as e:
    print(f"输入的不是数字，异常信息：{e}")
except ZeroDivisionError as e:
    print(f"除数不能为0，异常信息：{e}")
finally:
    print("程序结束")