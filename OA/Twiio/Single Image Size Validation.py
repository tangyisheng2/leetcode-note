#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :Single Image Size Validation.py
# @Time      :11/7/21 9:25 AM
# @Author    :Eason Tang

class Solution:
    def singal_image_size_validation(self, imageurls, maxSize):
        max_size_in_byte = self.get_maxSize(maxSize)
        ans = []
        if len(imageurls) >= 1:
            for imageurl in imageurls:
                url = imageurl[0]
                size = imageurl[1]
                ans.append([url, str(int(size) < max_size_in_byte)])

        return ans

    def _get_maxSize_(self, maxSize):
        if maxSize is None:
            return 1e6
        ans = 0
        num = int(maxSize[:-2])
        if maxSize[-2] == 'K' or maxSize[-2] == 'k':
            ans = num * 1e3
        elif maxSize[-2] == 'M' or maxSize[-2] == 'm':
            ans = num * 1e6
        elif maxSize[-2] == 'G' or maxSize[-2] == 'g':
            ans = num * 1e9

        return ans


test = Solution()
ret = test.singal_image_size_validation([['https://www.baidu.com/1.jpg', '32000000'],
                                         ['https://www.baidu.com/1.jpg', '32000000'],
                                         ['https://www.baidu.com/1.jpg', '32000000']], '40MB')
print(ret)