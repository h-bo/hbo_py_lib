
# coding:utf-8
# 读取数据表
# improved from https://github.com/nickzhangf/machine-learning/blob/61290fdc62f071a6ce58a217e019820e531fecfd/src/file2matrix.py
# wrong rows will be ignored

import sys
import os
from numpy import *

reload(sys)
sys.setdefaultencoding('utf-8')
def data2matrix(path, delimiter):
    recordList = []
    fp = open(path, 'rb')
    content = fp.read()
    fp.close()
    rowList = content.splitlines()
    for row in rowList:
        if row.strip():
            try:
                recordList = recordList + [map(eval, row.split(delimiter)) ]
            except Exception as e:
                print('Error:', e)
    return mat(recordList)

# to test: 
# recordMat = data2matrix('testtxt.txt', '\t')
# print shape(recordMat)
# print recordMat