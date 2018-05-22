# -*- coding: utf-8 -*-
# Project: maxent-ml
# Author: chaoxu create this file
# Time: 2018/2/28
# Company : Maxent
# Email: chao.xu@maxent-inc.com


def flatten(nestedList):
    # Write your code here
    x = []
    for i in nestedList:
        print("----{0}".format(i))
        if isinstance(i, list):
            x.extend(flatten(i))
        else:
            x.append(int(i))
    print("++", x)
    return x


if __name__ == '__main__':
    print(flatten([[1,1],2,[1,1]]))