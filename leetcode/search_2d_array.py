# -*- coding: utf-8 -*-
# Project: maxent-ml
# Author: chaoxu create this file
# Time: 2018/3/1
# Company : Maxent
# Email: chao.xu@maxent-inc.com


def searchMatrix(matrix, target):
    # write your code here
    xlow = 0
    xhigh = len(matrix) - 1
    while xlow <= xhigh:
        mid = (xlow + xhigh) // 2
        if target == matrix[mid][0] :
            return True
        elif target < matrix[mid][0]:
            xhigh = mid - 1
        elif target == matrix[mid][-1] :
            return True
        elif target > matrix[mid][-1]:
            xlow = mid+1
        else:
            ylow = 0
            yhigh = len(matrix[mid]) - 1
            while ylow <= yhigh:
                ymid = (ylow + yhigh) // 2
                match = matrix[mid][ymid]
                if target == match:
                    return True
                elif target < match:
                    yhigh = ymid - 1
                else:
                    ylow = ymid + 1
            return False
    return False


if __name__ == '__main__':
    a = [[1, 3, 5, 7],
         [10, 11, 16, 20],
         [23, 30, 34, 50]]
    b = [[5]]
    c = []
    print(searchMatrix(a, 33))
    # print(searchMatrix(b, 2))
    # print(searchMatrix(c, 2))
