#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re
import urllib
import time
# import sys

def getImg(path, html):
    reg = r'src="(.+?\.jpg)"'
    imgre = re.compile(reg)
    imglist = imgre.findall(html)
    
    x = 0
    for imgurl in imglist:
        print imgurl
        urllib.urlretrieve(imgurl, path + '\\%s.jpg' % x)
        x = x + 1
        # 延时1s
        time.sleep(1)

if __name__ == "__main__":
    # print sys.argv[1]
    # print ''.join(sys.argv[2:])
    html = ''
    path = ''
    getImg(path, html)