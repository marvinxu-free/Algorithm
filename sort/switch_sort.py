# -*- coding: utf-8 -*-
# Project: ml_more_algorithm
# Author: chaoxu create this file
# Time: 2018/5/22
# Company : Maxent
# Email: chao.xu@maxent-inc.com
"""
交换排序也叫冒泡排序，是一个非常经典的排序算法，主要思想如下：
1. 比较相邻的元素
2，如果相邻元素存在逆序对的时候，交换他们
3. 通过反复比较，最终完成排序

"""
import copy
import numpy as np


def switch_sort(a):
    """

    :param a:
    :return:
    """
    a = copy.deepcopy(a)
    for i in range(len(a)):  # 控制轮次
        sort_flg = False
        for j in range(1, len(a) - i):  # 控制相邻元素逆序交换, 因为每一轮将最大元素放到列表末端，所以后续不需要再去交换已经排序的最大元素
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]
                sort_flg = True
            if not sort_flg:
                break
    return a


if __name__ == '__main__':
    a = np.random.randint(1, 10, 5).tolist()
    b = switch_sort(a)
    print(f'{a} sorted to {b}')
