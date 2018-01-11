"""
二分查找, 前提是一个有序的元素列表. O(logn)
"""


def binary_search(list_temp, item):
    """
    二分查找
    :param list_temp: 有序列表
    :param item: 需要查找的元素
    :return: 查到返回index，否则返回 None
    """
    low = 0  # 跟踪查找的低位 index
    high = len(list_temp) - 1  # 跟踪查找的高位 index
    while low <= high:
        mid = int((low + high) / 2)
        guess = list_temp[mid]  # 获取中间到元素
        print('guess', mid, guess)
        if guess == item:  # 如果是检查的元素，返回 index
            return mid
        elif guess > item:  # 如果大于需要查找的元素，高位index缩小到中间以下
            high = mid - 1
        else:
            low = mid + 1  # 如果小于需要查找的元素，低位index扩大到中间以上
    return None


data_list = list(range(0, 101, 7))
print(data_list)
index = binary_search(data_list, 7)
print(index)
