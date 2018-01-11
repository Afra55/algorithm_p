"""
快速排序, 平均时间 O(nlogn)，最糟糕时间 O(n^2)
基本思想：通过一趟排序将要排序的数据分割成独立的两部分，其中一部分的所有数据都比另外一部分的所有数据都要小，
然后再按此方法对这两部分数据分别进行快速排序，整个排序过程可以递归进行，以此达到整个数据变成有序序列。
"""
from random import shuffle, randrange


def quick_sort_pivot_is_first(arr):
    """
    以第一个点作为基准
    :param arr: 列表
    :return: 有序列表
    """
    if len(arr) <= 1:
        return arr  # 为空或只有一个元组的数组是'有序'的
    else:
        pivot = arr[0]  # 基准值
        less = [i for i in arr[1:] if i <= pivot]  # 所有小于等于基准值的元素组成子组
        greater = [i for i in arr[1:] if i > pivot]  # 所有大于基准值的元素组成的子组
        return quick_sort_pivot_is_first(less) + [pivot] + quick_sort_pivot_is_first(greater)


def quick_sort_pivot_is_center(arr):
    """
    以中心点作为基准
    :param arr: 列表
    :return: 有序列表
    """
    if len(arr) <= 1:
        return arr  # 为空或只有一个元组的数组是'有序'的
    else:
        center_index = int((len(arr) - 1) / 2)
        pivot = arr[center_index]  # 以中心点为基准值
        arr_exclude_center = arr[:center_index] + arr[center_index + 1:]
        less = [i for i in arr_exclude_center if i <= pivot]  # 所有小于等于基准值的元素组成子组
        greater = [i for i in arr_exclude_center if i > pivot]  # 所有大于基准值的元素组成的子组
        return quick_sort_pivot_is_center(less) + [pivot] + quick_sort_pivot_is_center(greater)


def quick_sort_pivot_is_random(arr):
    """
    以随机点作为基准
    :param arr: 列表
    :return: 有序列表
    """
    if len(arr) <= 1:
        return arr  # 为空或只有一个元组的数组是'有序'的
    else:
        random_index = randrange(0, len(arr))
        pivot = arr[random_index]  # 基准值
        arr_exclude_random_index = arr[:random_index] + arr[random_index + 1:]
        less = [i for i in arr_exclude_random_index if i <= pivot]  # 所有小于等于基准值的元素组成子组
        greater = [i for i in arr_exclude_random_index if i > pivot]  # 所有大于基准值的元素组成的子组
        return quick_sort_pivot_is_random(less) + [pivot] + quick_sort_pivot_is_random(greater)


def quick_sort(arr, low, high):
    """
    三路基数快排
    :param arr: 列表
    :param low: 左边界
    :param high: 右边界
    :return: 有序列表
    """
    i = low  # i 初始化未左边界 index，用于从左往右遍历, 动态左边界
    j = high  # j 初始化未右边界 index，用于从右往左遍历，动态右边界
    if i >= j:
        return arr
    pivot = arr[i]  # 以待排列表的第一个元素作为基准值, 即取出 i 处的值
    while i < j:  # i 和 j 未碰撞时循环
        while j > i and arr[j] >= pivot:  # 从 j 往 i 遍历, 减小 j 值，找到小于基准值的 index
            j = j - 1
        arr[i] = arr[j]  # 取出 j 处的值放在 i 处，即将获得的小于基准值的该值放在 i 处
        while i < j and arr[i] <= pivot:  # 从 i 往 j 遍历, 增加 i 值，找到大于基准值的 index
            i = i + 1
        arr[j] = arr[i]  # 取出 i 处的值放在 j 处，即将获得的大于基准值的该值放在 j 处
    arr[i] = pivot  # 把基准值放在 i 处，此时的 i == j， 处于列表的中心点
    quick_sort(arr, low, i - 1)  # 排序中心点左边的列表，即小于基准点的列表
    quick_sort(arr, i + 1, high)  # 排序中心点右边的列表，即大于基准点的列表
    return arr  # 返回有序数组


random_data = list(range(100))
shuffle(random_data)
print('无序列表:', random_data)
print('排序后：', quick_sort(random_data, 0, len(random_data) - 1))
