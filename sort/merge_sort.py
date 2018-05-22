# -*- coding: utf-8 -*-
# Project: ml_more_algorithm
# Author: chaoxu create this file
# Time: 2018/5/22
# Company : Maxent
# Email: chao.xu@maxent-inc.com
"""
归并排序目的是把多个有序序列合并成一个排序序列,以二路归并排序为例：
1. 初始时把待排序序列当成n个有序子序列，也就是每一个元素自身是有序的
2. 把序列里面的有序子序列两两归并，完成一次后，里面的子序列数量减半，每个子序列的长度加一
3. 对加上的子序列重复以上的操作
"""

import copy
import numpy as np


def mergesort(seq):
    """归并排序"""
    if len(seq) <= 1:
        return seq
    mid = len(seq) // 2  # 将列表分成更小的两个列表
    # 分别对左右两个列表进行处理
    left = mergesort(seq[:mid])
    right = mergesort(seq[mid:])
    # 对排序好的两个列表排序合并，产生一个新的排序好的列表
    return merge(left, right)


def merge(left, right):
    """合并两个已排序好的列表，产生一个新的已排序好的列表"""
    result = []  # 新的已排序好的列表
    i = 0  # 下标
    j = 0
    # 对两个列表中的元素 两两对比。
    # 将最小的元素，放到result中，并对当前列表下标加1
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


if __name__ == '__main__':
    # seq = np.random.randint(1, 100, 20).tolist()
    seq = [25, 67, 54, 33, 20, 78, 65, 49, 17, 56, 44]
    print(f'排序前:f{seq}')
    result = mergesort(seq)
    print(f'排序后：f{result}')
