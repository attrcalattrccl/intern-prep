# 1、去重 + 排序
# s = {3, 1, 4, 1, 5, 9, 2, 6, 5, 3}
# L = list(s)
# L.sort()
# print(L)

# 2、字符计数
# text = 'hello'
# dict_text = {}
# for i in text:
#     dict_text[i] = dict_text.get(i, 0) + 1      
#     # 查询字典中是否含i：
#     # 不含则返回默认值0，+1后得到1这一value，与i这一key存入字典
#     # 含则返回对应value（1），+1后存回value（2）。从而value存的就是i出现的次数了
# print(dict_text)

# 通讯录雏形
# address_list = {'p1':12341, 'p2':12342, 'p3':12343}
# search_p = input("请输入人名：")
# if search_p in address_list:
#     search_num = address_list[search_p]
#     print(f"{search_p}的号码是：{search_num}")
# else:
#     print(f"未查询到{search_p}的信息")