# -*- coding: utf-8 -*-
# Project: ml_more_algorithm
# Author: chaoxu create this file
# Time: 2018/5/22
# Company : Maxent
# Email: chao.xu@maxent-inc.com
"""
插入排序是排序中最简单的一个，基本思想就是:
通过按下标在连续表的前端或者后端积累已经排序的序列,
通过这个序列的不断生长，最终完成排序

关键在于把待处理元素插入到已排序列表的合适位置
"""

import copy


def insert_sort(a):
    """
    连续表的前端不断积累
    :param a: a list wait for sort
    :return:
    """
    a = copy.deepcopy(a)
    for i in range(0, len(a)):
        x = a[i]
        j = i
        while j > 0 and a[j - 1] > x:
            a[j] = a[j - 1]  # 反序逐个后移元素，知道找到不需要后移的点，即为插入位置
            j -= 1
        a[j] = x
    return a


def insert_sort1(a):
    """
    连续表的后端不断积累
    :param a: a list wait for sort
    :return:
    """
    a = copy.deepcopy(a)
    for i in reversed(range(0, len(a))):
        x = a[i]
        j = i
        while j > 0 and a[j - 1] > x:
            a[j] = a[j - 1]
            j -= 1
        a[j] = x
    return a


if __name__ == '__main__':
    a = [2, 3, 6, 1]
    b = insert_sort(a)
    c = insert_sort1(a)
    print(f'{a} sorted to {b} and {c}')
