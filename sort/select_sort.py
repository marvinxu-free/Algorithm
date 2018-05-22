# -*- coding: utf-8 -*-
# Project: ml_more_algorithm
# Author: chaoxu create this file
# Time: 2018/5/22
# Company : Maxent
# Email: chao.xu@maxent-inc.com
"""
选择排序的基本思想是：
1. 维护一个已经排序的列表，保证已排序列表里面的元素都小于未排序列表的元素
2. 每次从未排序的列表里面扫描，选择最小的一个元素附在已排序列表的后面
3. 当未排序列表只剩一个的时候，必然是最大的元素

如何不增加额外列表的情况下，腾出已排序列表的位置，
直接选择排序法通过直接交换当前判断的元素和未排序列表里面的最小原色
"""
import copy


def direct_select_sort(a):
    """

    :param a:
    :return:
    """
    a = copy.deepcopy(a)
    for i in range(0, len(a)):
        k = i
        for j in range(i, len(a)):
            if a[j] < a[k]:
                k = j

        if i != k:
            a[i], a[k] = a[k], a[i]
    return a


def heap_select_sort(a):
    """

    :param a:
    :return:
    """
    pass


if __name__ == '__main__':
    a = [2, 4, 3, 1, 6]
    b = direct_select_sort(a)
    print(f"{a} soted to {b}")
