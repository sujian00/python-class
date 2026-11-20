"""实验三：列表、字典与曼哈顿距离"""


def read_int_list(prompt):
    """读取整数列表，支持英文逗号、中文逗号或空格分隔。"""
    text = input(prompt).strip()
    if not text:
        return []

    text = text.replace("，", ",")
    parts = text.split(",") if "," in text else text.split()
    return [int(item.strip()) for item in parts if item.strip()]


def print_title(number, title):
    """打印每道题的醒目分隔标题。"""
    print("\n" + "=" * 60)
    print(f"第 {number} 题：{title}")
    print("=" * 60)


def task1():
    print_title(1, "用两个列表生成字典")
    lst_a = read_int_list("请输入列表 lstA（整数用逗号或空格分隔）：")
    lst_b = read_int_list("请输入列表 lstB（整数用逗号或空格分隔）：")

    count = min(len(lst_a), len(lst_b))
    result = dict(zip(lst_a[:count], lst_b[:count]))

    print("生成的字典：", result)
    print("字典元素个数：", len(result))
    print("说明：元素个数由较短的列表决定；如果 lstA 中有重复元素，字典的键会自动去重。")


def task2():
    print_title(2, "列表降序排列")
    lst = read_int_list("请输入一个整数列表（整数用逗号或空格分隔）：")
    new_lst = sorted(lst, reverse=True)
    print("降序排列后的新列表：", new_lst)


def task3():
    print_title(3, "列表元素连乘")
    lst = read_int_list("请输入一个整数列表（整数用逗号或空格分隔）：")

    if not lst:
        print("列表为空，无法计算连乘结果。")
        return

    product = 1
    for number in lst:
        product *= number
    print("连乘结果：", product)


def task4():
    print_title(4, "曼哈顿距离")
    point1 = read_int_list("请输入第一个坐标（两个整数，用逗号或空格分隔）：")
    point2 = read_int_list("请输入第二个坐标（两个整数，用逗号或空格分隔）：")

    if len(point1) != 2 or len(point2) != 2:
        print("每个坐标必须包含 2 个整数。")
        return

    distance = abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
    print("两点之间的曼哈顿距离：", distance)


def main():
    task1()
    task2()
    task3()
    task4()


if __name__ == "__main__":
    main()
