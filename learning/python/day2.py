# 第一块：if/elif/else
# 1.成绩分档
# score = int(input("成绩："))

# if score >= 90:
#     print(f"{score}————A")
# elif score >= 80:
#     print(f"{score}————B")
# elif score >= 60:
#     print(f"{score}————C")
# else:
#     print(f"{score}————D")

# 2.判断闰年
# year = int(input("年份："))

# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(f"{year} 是闰年")
# else:
#     print(f"{year} 是平年")

# 3.三个数的最大值
# num1 = int(input("num1 = "))
# num2 = int(input("num2 = "))
# num3 = int(input("num3 = "))

# if num1 >= num2 and num1 >= num3:
#     print(f"max = {num1}")
# elif num2 >= num1 and num2 >= num3:
#     print(f"max = {num2}")
# else:
#     print(f"max = {num3}")

# 第二块：循环
# 1. 打印1到10
# for i in range(1,11):
#     print(i)

# 2. 1 到 100 求和（累加器）
# total = 0
# total_even = 0
# for i in range(1,101):
#     total += i
#     if i % 2 == 0:
#         total_even += i
# print(total, total_even)

# 3. 九九乘法表（嵌套循环）
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print(f"{j} * {i} = {i * j}", end="  ")
#     print()