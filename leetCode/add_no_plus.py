# -*- coding: utf-8 -*-
# Project: maxent-ml
# Author: chaoxu create this file
# Time: 2018/2/28
# Company : Maxent
# Email: chao.xu@maxent-inc.com


import ctypes
class Solution:
    """
    @param a: An integer
    @param b: An integer
    @return: The sum of a and b
    """
    def aplusb(self, a, b):
        while b != 0:
            carry = (a & b) << 1
            s = a ^ b
            a = s
            b = carry
        return a


if __name__ == '__main__':
    a = Solution()
    print(a.aplusb(100, -100))

