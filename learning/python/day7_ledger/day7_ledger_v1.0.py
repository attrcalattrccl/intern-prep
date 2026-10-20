import json
import os
from datetime import date

# 设计：
# 列表套字典，一条一条记录（字典），录在一个大列表内
# 5个功能——5个函数:查询全部（1）、记一笔（1）、统计（1）、类别编辑[添加（1）、删除（1）、重命名（1）]
# 基础函数：写入文件（1）、选择类别（1）、遍历打印类别（1）

# 相对路径
BASE = os.path.dirname(os.path.abspath(__file__))

# 写入文件，（内容，路径）——>写入
def write_in_file(content,f_path):
    with open(f_path, "w", encoding="utf-8") as f:
        json.dump(content, f, ensure_ascii=False, indent=2)

# 1. 查询全部记录：返回记录（用于读取records和categories）
def show_all(f_path):
    try:
        with open(f_path, "r", encoding="utf-8") as f:
            re_all = json.load(f)
        return re_all
    except FileNotFoundError:
        no_f = []
        return no_f

# 前加序号遍历打印列表
def traverse_print(con):        # 填入要循环打印的列表为参数
    i = 0
    for ch in con:     
        print(f"{i}.{con[i]}")
        i += 1

# 选择类别 函数
def choose_category(ca_list, ca_1):
    traverse_print(ca_1)
    ch_1 = int(input("请选择大类（阿拉伯数字、不加符号）："))
    while ch_1 != 0 and ch_1 != 1:
        ch_1 = int(input("没有该选项，请重新选择："))
    ca_2 = ca_list.get(ca_1[ch_1])
    traverse_print(ca_2)
    ch_2 = int(input("请选择类别（阿拉伯数字、不加符号）："))
    while ch_2 < 0 or ch_2 >= len(ca_2) :
        ch_2 = int(input("没有该选项，请重新选择："))
    ch_ca = (ch_1, ca_2[ch_2], ch_2)      # 得到元组，第0个是金第一层的选择序号：ca_1(ch_1)（支出1或收入0）；第1个为类别字符串；第2个为第二层的选择序号
    return ch_ca
    
    
# 2.记一笔
def make_an_entry(records):          
    today = str(date.today())
    print(f"今天日期为：{today}")
    ca_tu = choose_category(ca_list, ca_1)
    amount = float(input("金额（元）（>= 0）："))
    while amount < 0:
        amount = float(input("请输入非负数"))
    note = input("请输入备注：")
    obj = {"date":today, 
           "amount":(-1) ** ca_tu[0] * amount, 
           "category":[ca_1[ca_tu[0]], ca_tu[1]], 
           "note":note}
    records.append(obj)
    write_in_file(records, PATH_records)
    print("记录成功~")
    return records

# 3. 统计总合计、总收入、总支出、各分类合计（从后往前计）
def get_total(records, ca_list, ca_1):
    # 计算分类合计
    sig_to = {}         # 新建一个空字典放分类合计
    for ca1 in ca_1:                        # 分别循环两个大类作为key
        for sig in ca_list.get(ca1):        # 再循环选择的大类作为的key对应的value列表——细分类别列表
            sig_to[sig] = 0                 # 将每一分类作为key，value设成0，存入分类合计字典中
    for sig in records:                     # 循环每条record(sig是每条records)
        n = sig["category"][1]
        sig_to[n] = sig_to.get(n, 0) + sig["amount"]
    # 计算总合计、总收入、总支出
    am_to = 0
    in_to = 0
    ex_to = 0
    for sig in records:
        if sig["amount"] > 0:
            in_to += sig["amount"]
        else:
            ex_to += sig["amount"]
        am_to += sig["amount"]
    # 得到total字典
    to_dirt = {"总合计":am_to, "总收入":in_to, "总支出":ex_to, "各分类合计":sig_to}
    return to_dirt

# 4.1 添加类别
def add_category(ca_list, ca_1):
    traverse_print(ca_1)
    ch_1 = int(input("请选择大类（阿拉伯数字、不加符号）："))
    while ch_1 != 0 and ch_1 != 1:
        ch_1 = int(input("没有该选项，请重新选择："))
    add_name = input("请输入新类别名称：")
    if add_name in ca_list.get(ca_1[ch_1]):
        print(f"已有{add_name}")
    else:
        ca_list.get(ca_1[ch_1]).append(add_name)         # 直接将新类别名添加进对应大类的细分列表后
        write_in_file(ca_list, PATH_categories)         # 立即写回
        ca_list = show_all(PATH_categories)             # 重新读一遍caregories.json，确保程序内的ca_list始终与文件内同步
        print(f"{ca_1[ch_1]}类别有：{ca_list[ca_1[ch_1]]}")                   
    return ca_list        # 返回新ca_list以更新已读取的ca_list

# 4.2 删除类别
def del_category(ca_list, ca_1):
    del_ca = choose_category(ca_list, ca_1)      
    reconfirm = input(f"确认删除{del_ca[1]}(y/n): ")
    if reconfirm == "y":
        ca_list.get(ca_1[del_ca[0]]).remove(del_ca[1])
        write_in_file(ca_list, PATH_categories)
        ca_list = show_all(PATH_categories)         # 重新读一遍caregories.json，确保程序内的ca_list始终与文件内同步
        print(f"{ca_1[del_ca[0]]}类别有：{ca_list[ca_1[del_ca[0]]]}")
    else:
        print("类别删除已取消")
    return ca_list      # 返回新ca_list以更新已读取的ca_list

# 4.3 重命名类别
def rename_category(ca_list, ca_1):
    ren_ca = choose_category(ca_list, ca_1)
    new_name = input("请输入新的名称：")
    if new_name in ca_list.get(ca_1[ren_ca[0]]):
        print(f"{new_name}类别已存在")
    else:
        reconfirm = input(f"确认重命名\"{ren_ca[1]}\"为 \"{new_name}\"(y/n)：")
        if reconfirm == "y":
            ca_list.get(ca_1[ren_ca[0]]).remove(ren_ca[1])                  # 删掉列表原来元素
            ca_list.get(ca_1[ren_ca[0]]).insert(ren_ca[2], new_name)        # 插入新命名的元素
            write_in_file(ca_list, PATH_categories)
            ca_list = show_all(PATH_categories)         # 重新读一遍caregories.json，确保程序内的ca_list始终与文件内同步
            print(f"{ca_1[ren_ca[0]]}类别有：{ca_list[ca_1[ren_ca[0]]]}")
        else:
            print("类别重命名已取消")
    return ca_list      # 返回新ca_list以更新已读取的ca_list

# 询问用户操作语句
opts = """这里是您的记账本~~
\t1.查询全部记录
\t2.记一笔
\t3.统计总支出、总收入 + 各分类合计
\t4.类别编辑
\t5.退出
请选择您要进行的操作（阿拉伯数字、不加符号）："""

# main
PATH_records = os.path.join(BASE, "records.json")    #得到record.json的相对路径
PATH_categories = os.path.join(BASE, "categories.json")     #得到category的相对路径

ca_1 = ("income","expense")
# # 类别初始化（仅运行第一次）（类别固定，便于计算合计）（已测试成功）
# # 第一层：收入/支出（不可更改，作为全局常数）（L79）     
# # 第二层：
# ca_ex = ["food & dining", "transportation", "housing", "shopping", "entertainment", "medical", "education", "gifts & red envelopes", "others"]
# ca_in = ["salary", "bonus", "side income", "investment income","cash gift", "others"]
# # 整体二层框架（字典）
# ca_st = {ca_1[0]:ca_in, ca_1[1]:ca_ex}
# # 类别写入json
# write_in_file(ca_st, PATH_categories)


# 程序初始化：先读取一次records、categories
records = show_all(PATH_records)
ca_list = show_all(PATH_categories)

while 1==1:
    try:
        todo = input(opts)
        match todo:
            case "1":
                for i in records:
                    print(f"日期：{i['date']}\t金额：{i['amount']}\t类别：{i['category'][0]}-{i['category'][1]}\t备注：{i['note']}")
            case "2":
                records = make_an_entry(records)        # 读取在外面的records也要更新
            case "3":
                to_dirt = get_total(records, ca_list, ca_1)
                print(f"您的总合计为{to_dirt['总合计']}\n总收入为{to_dirt['总收入']}\n总支出为{to_dirt['总支出']}\n各分类合计为{to_dirt['各分类合计']}")
            case "4":
                opt = input("0.添加类别\t1.删除类别\t2.类别重命名\t3.读取类别\n请选择要进行的操作（阿拉伯数字、不加符号）：")
                match opt:
                    case "0":       # 添加类别
                        ca_list = add_category(ca_list, ca_1)       # 进行添加并更新ca_list
                    case "1":       # 删除类别
                        ca_list = del_category(ca_list, ca_1)
                    case "2":       # 类别重命名
                        ca_list = rename_category(ca_list, ca_1)
                    case "3":
                        print(ca_list)
            case "5":
                print("程序结束，再见~~")
                break
            case _:
                print("输入错误，请重新选择")
    except ValueError:
        print("错误，请输入阿拉伯数字")
    # except Exception as e:
    #     print(f"程序出错，请联系管理员。错误信息：{e}")