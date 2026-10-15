# 1. 最简单的函数
# def say_hello():
#     print("hello")

# say_hello()

# 2. 带参数、有返回值
# def add(a, b):
#     return a + b

# result = add(3, 5)
# print(result)

# 3. 没有return的函数，返回值是None
# def no_return():
#     print("我只负责打印")

# x = no_return()
# print(x)

# 4. 返回圆面积
# def circle_area(r):
#     return 3.14159 * r **2
# print(circle_area(float(input("r = "))))

# 5. 判断闰平年
# def is_leap(year):
#     return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

# print(is_leap(int(input("year = "))))

# 6. 传入列表返回最大值
# def find_max(nums):
#     m = nums[0]
#     for i in nums:
#         if m < i:
#             m = i
#     return m

# print(find_max([3, 7, 2, 9]))     
# print(find_max([-5, -1, -9]))