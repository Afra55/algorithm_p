"""
贪婪算法，一种近似算法
每步都选择局部最优解，最终获得全局最优解
解决NP完全问题
NP完全问题: 难解问题，如商旅问题，覆盖问题
"""


def get_best_keys(nums, nums_needed):
    """
    找出 nums散列表 中，覆盖 nums_needed 所需 number 的最优 key
    :param nums:
    :param nums_needed:
    :return:
    """

    final_keys = set()  # 存储最终获取到的 key

    while nums_needed:  # 当所需集合不为空时，进入循环
        best_key = None  # 存储最优 key
        numbers_covered = set()  # 最优 key 对应的数字中覆盖了所需的数字

        for key, numbers_for_key in nums.items():  # 遍历 key-numbers 散列表
            covered = nums_needed & numbers_for_key  # 取交集，即两个集合都有的数字
            if len(covered) > len(numbers_covered):  # 如果该 key 对应的数字集合包含所需的数字更多时，这个key时最优key
                best_key = key
                numbers_covered = covered

        nums_needed -= numbers_covered  # 剔除需求集合中已被覆盖的数字集合
        final_keys.add(best_key)  # 获取到最终的 key

    print(final_keys)  # 输出覆盖了所有所需数字集合的最优 key


# noinspection PySetFunctionToLiteral
def number_test():
    numbers_needed = set([1, 2, 3, 4, 5, 6, 7, 8])  # 需要的数字集合
    # noinspection PyDictCreation
    numbers = {}
    numbers['one'] = set([1, 2, 3])
    numbers['two'] = set([4, 1, 5])
    numbers['three'] = set([6, 2, 7])
    numbers['four'] = set([2, 3])
    numbers['five'] = set([7, 8])

    get_best_keys(numbers, numbers_needed)


if __name__ == '__main__':
    number_test()
