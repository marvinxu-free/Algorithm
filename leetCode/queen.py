# -*- coding: utf-8 -*-
# Project: maxent-ml
# Author: chaoxu create this file
# Time: 2018/2/27
# Company : Maxent
# Email: chao.xu@maxent-inc.com
"""
this funtion used to solve 8 queens problems
"""


def chk_pos(queen_state, next_pos):
    """

    :param state:
    :param next_pos:
    :return:
    """
    for i, j in enumerate(queen_state):
        k1 = j - next_pos[1]
        k2 = i - next_pos[0]
        k = abs(k1 / k2)
        if i == next_pos[0] or j == next_pos[1] or k == 1 :
            return True
        else:
            return False


def queens(num, queen_state=[]):
    """

    :param num:
    :param queen_state:
    :return:
    """
    if len(queen_state) == num - 1:
        print('queen placed')
        return True
    else:
        for i in range(num):


