# -*- coding: utf-8 -*-
# Project: ml_more_algorithm
# Author: chaoxu create this file
# Time: 2018/5/22
# Company : Maxent
# Email: chao.xu@maxent-inc.com
"""
快速排序是一种著名的排序算法，最早是采用递归的方式描述的一种有没算法。
在各种排序算法中，是平均速度最快的一种算法, 基本过程如下：
1. 选择一个标准，将原始列表分成两个大小两组
2. 重复以上过程， 递归的得到两组列表，并重复下去
3. 如果划分得到的列表为空，返回空列表，递归按照栈操作退出
4. 当回到最初调用栈时，将两个大小列表以及标准拼成一个列表
"""
import sys

sys.setrecursionlimit(1500)
import copy
import numpy as np


def recursive_quick_sort(a):
    """

    :param a:
    :return:
    """
    if len(a) == 0:
        return []
    else:
        pivot = a[0]
        left = recursive_quick_sort([x for x in a[1:] if x < pivot])
        right = recursive_quick_sort([x for x in a[1:] if x >= pivot])
    return left + [pivot] + right


if __name__ == '__main__':
    a = np.random.randint(1, 10, 5).tolist()
    b = copy.deepcopy(a)
    recursive_quick_sort(b)
    print(f'{a} sorted to {b}')
