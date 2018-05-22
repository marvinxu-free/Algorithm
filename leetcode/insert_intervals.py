# -*- coding: utf-8 -*-
# Project: maxent-ml
# Author: chaoxu create this file
# Time: 2018/3/1
# Company : Maxent
# Email: chao.xu@maxent-inc.com
from copy import deepcopy


def insert(intervals, newInterval):
    # write your code here

    new_list = deepcopy(intervals)
    new_list.append(newInterval)
    del_i = []
    for i in range(len(new_list)):
        flg = False
        for j in range(1, len(new_list) - i):
            if new_list[j - 1][0] > new_list[j][-1]:
                new_list[j - 1], new_list[j] = new_list[j], new_list[j - 1]
            elif new_list[j - 1][-1] >= new_list[j][0]:
                tmp = list(set(new_list[j - 1] + new_list[j]))
                s = [tmp[0], tmp[-1]]
                new_list[j - 1], new_list[j] = s, s
                del_i.append(j)
            elif new_list[j][0] <= new_list[j - 1][0] and new_list[j][-1] >= new_list[j - 1][-1]:
                new_list[j - 1] = new_list[j]
                del_i.append(j)
            elif new_list[j - 1][0] <= new_list[j][0] and new_list[j - 1][-1] >= new_list[j][-1]:
                new_list[j] = new_list[j - 1]
                del_i.append(j)
    for i in del_i:
        del new_list[i]
    return new_list


if __name__ == '__main__':
    print(insert([[1, 5]], [2, 3]))
