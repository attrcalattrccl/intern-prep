import os

Dir = r"learning\python\day6_rename"
file_to_change = [x for x in os.listdir(Dir) if x.endswith(".txt") and not x.startswith("new_")]           # 只保留了.txt文件
print(file_to_change)       # 检查是否只保留了不是new_开头的.txt文件

if input("确认执行？（y/n）：") != "y":
    exit()

for f_o in file_to_change:
    f_n = "new_" + f_o
    d_o = os.path.join(Dir, f_o)
    d_n = os.path.join(Dir, f_n)
    os.rename(d_o, d_n)
    print(f"已将{f_o}更名为{f_n}")