"""
选择排序
"""
from random import shuffle


def findsmallest(arr):
    """
    获取列表中最小值的 index
    :param arr: 列表
    :return: index
    """
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selection_sort(arr):
    """
    选择排序
    :param arr: 列表
    :return: 排序后的列表
    """
    new_arr = []
    for i in range(len(arr)):
        smallest_index = findsmallest(arr)
        new_arr.append(arr.pop(smallest_index))
    return new_arr


random_data = list(range(100))
shuffle(random_data)
print('无序列表:', random_data)
print('排序后：', selection_sort(random_data))
