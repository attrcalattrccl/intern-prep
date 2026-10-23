import json
import os

BASE = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(BASE, "week1_contacts.json")

# contacts——ct; search——se; delete——del; option——opt; reconfirm——recf

# 基础函数
# 读取json文件：PATH ——> 列表
def read_file(PATH):
    try:
        with open(PATH, "r", encoding="utf-8") as f:
            ct = json.load(f)
    except FileNotFoundError:       # 文件不存在时返回空列表
        ct = []
    return ct

# 写入json文件：
def write_in(PATH, ct):
    with open(PATH, "w", encoding="utf-8") as f:
        json.dump(ct, f, ensure_ascii=False, indent=2)

# 功能函数
# 1.按姓名查询：ct,name ——> (姓名，电话号码，记录索引)
def se_name(ct, name):
    ind = 0
    for c in ct:
        if c.get("name") == name:
            phone = c.get("phone")
            return (name, phone, ind)
        else:
            ind += 1
    return None


# 2.添加联系人：
def add_ct(ct, PATH, name, phone):                   # 返回ct以更新启动初始化ct
    ct.append({"name":name, "phone":phone})
    write_in(PATH, ct)
    print("添加成功")
    return ct

# 2.1 add执行系统：
def add_exe(ct, PATH, name, phone):
    se_ret = se_name(ct, name)          # 查询是否存在该联系人
    if se_ret != None:                  # 存在联系人
        while 1 == 1:
            recf = input(f"{se_ret[0]}已存在，电话号码为{se_ret[1]}，是否更改电话号码(y/n)：")
            match recf:
                case "y":
                    ct[se_ret[2]]["phone"] = phone
                    write_in(PATH, ct)
                    print("更改成功")
                    return ct
                case "n":
                    print("添加联系人已取消")
                    return ct
                case _:
                    print("请输入y(yes)或n(no)")
    else:                               # 不存在联系人
        ct = add_ct(ct, PATH, name, phone)
        return ct
    
# 3.显示全部联系人
def show_all(ct):
    for c in ct:
        print(f"姓名：{c['name']}\t电话号码：{c['phone']}")

# 4.删除联系人
def del_ct(ct, PATH, name, se_ret):
    ct.pop(se_ret[2])
    write_in(PATH, ct)
    print("删除成功")

# 4.1 del执行系统
def del_exe(ct, name, PATH):            # 返回ct以更新启动初始化ct
    se_ret = se_name(ct, name)          # 查询是否存在该联系人
    if se_ret != None:                  # 存在联系人
        while 1 == 1:
            recf = input(f"确定删除 {se_ret[0]} {se_ret[1]} (y/n)：")
            match recf:
                case "y":
                    del_ct(ct, PATH, name, se_ret)
                    return ct
                case "n":
                    print("删除联系人已取消")
                    return ct
                case _:
                    print("请输入y(yes)或n(no)")
    else:                               # 不存在联系人
        print(f"请检查输入的姓名，未查询到{name}")
        return ct

# 启动初始化：读取contacts
ct = read_file(PATH)

# 菜单询问语句
ask_w = """
\t1.按姓名查询
\t2.添加联系人
\t3.显示全部联系人
\t4.删除联系人
\t5.保存并退出
请选择您要使用的功能（1-5，不带符号）：
"""

# main
while 1 == 1:
    opt = input(ask_w)
    match opt:
        case "1":       # 1.按姓名查询
            name = input("请输入要查询的联系人姓名：")
            se_ret = se_name(ct, name)        # 返回一个元组（name，phone, ind）/ None
            if se_ret != None:
                print(f"查询结果：\n姓名：{se_ret[0]}\t电话号码：{se_ret[1]}")
            else:
                print(f"未查询到{name}")
        case "2":       # 2.添加联系人
            name = input("请输入添加的联系人的姓名：")
            phone = input("请输入电话号码：")
            ct = add_exe(ct, PATH, name, phone)
        case "3":       # 3.显示全部联系人
            show_all(ct)
        case "4":       # 4.删除联系人
            name = input("请输入要删除的联系人姓名：")
            ct = del_exe(ct, name, PATH)
        case "5":       # 5.保存并退出
            print("程序结束，再见")
            break
        case _:
            print("请输入1-5阿拉伯数字，不带符号空格")