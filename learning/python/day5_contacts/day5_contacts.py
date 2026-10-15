import json
PATH = r"F:\实习\project\learning\python\day5_contacts\contacts.json"
# 初始化通讯录:(已完成)
# initial_contacts = {"小明":"1234561","小红":"1234562"}
# with open("F:\实习\project\learning\python\day5_contacts\contacts.json", "w", encoding="utf-8") as f:
#     json.dump(initial_contacts, f, ensure_ascii=False, indent=2)

# 读取通讯录：返回 json文件内容
def contacts_read():
    try:
        with open(PATH, "r", encoding="utf-8") as f:
            contacts = json.load(f)
    except FileNotFoundError:
        contacts = {}
    return contacts
    
# 人名查找号码：返回 号码/0
def contacts_search(contacts, name):
    return contacts.get(name)

# 添加到通讯录（基础程序）
def contacts_add_base(name,num):
    contacts[name] = num
    with open(PATH, "w", encoding="utf-8") as f:
        json.dump(contacts,f,ensure_ascii=False,indent=2)
    print("添加成功")

# 添加到通讯录（主结构）:询问name和number，判断是否已有联系人
def contacts_add():
    name = input("name: ")
    num = input("number: ")
    if name in contacts:        # 若通讯录内已有联系人
        update_inquiry = input("此人名已存在\n\t1.覆盖原号码\n\t2.更改新联系人姓名\n\t3.退出新增联系人\n请输入：")
        match update_inquiry:
            case "1":
                contacts_add_base(name,num)
            case "2":
                name = input("请输入新姓名：")
                contacts_add_base(name,num)
            case "3":
                print("已退出新增联系人")
            case _:
                print("输入不符合规定，已退出新增联系人")
    else:
        contacts_add_base(name,num)

# main:
# 询问用户需求语句
asking_words = ("""
这里是您的通讯录，请问您想进行的操作是：
\t1.获取通讯录名单
\t2.查询联系人
\t3.新增联系人
\t4.结束使用
请输入（1-4）：""")

#初始化，先读取一次
contacts = contacts_read()

while 1 == 1:
    opt = input(asking_words)
    match opt:
        case "1":
            print(contacts)
        case "2":
            name = input("请输入要查找的联系人姓名：")
            s_result = contacts_search(contacts, name)
            if s_result == None:
                print("没有这个人")
            else:
                print(s_result)
        case "3":
            contacts_add()
            contacts = contacts_read()      #更新读取到的contacts
        case "4":
            print("服务结束")
            break
        case _:
            print("输入不符合要求")