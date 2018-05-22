# -*- coding: utf-8 -*-
# Project: maxent-ml
# Author: chaoxu create this file
# Time: 2018/2/28
# Company : Maxent
# Email: chao.xu@maxent-inc.com


def binarySearch(nums, target):
    # write your code here
    num_len = len(nums)
    low = 0
    high = num_len - 1
    while low <= high:
        mid = (high + low) // 2
        mid_pre = max(mid - 1, 0)
        print(mid, mid_pre)
        if nums[mid] == target:
            if mid_pre > 0 and nums[mid] != nums[mid_pre]:
                return mid
            elif mid_pre == 0 and mid == 0:
                return 0
            else:
                if nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid_pre
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid_pre
    return -1


if __name__ == '__main__':
    a = binarySearch([3,4,5,8,8,8,8,10,13,14], 8)
    print(a)
