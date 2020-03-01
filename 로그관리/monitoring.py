#!/bin/env python
#-*- coding:utf-8 -*-

from mylog import get_log_data
from time import sleep
import os
import sys
import datetime

def check(file_name, search_word):
    if os.path.exists(file_name):
        print "모니터링 시작 :", file_name
        print "대상 :", search_word
        print "-" * 70
    else:
        print "찾으려는 파일이 없습니다 :", file_name

    index = 0
    while os.path.exists(file_name) :
        fp = open(file_name)
        file_data = fp.read()
        index = file_data.find(search_word, index)
        fp.close()

        if index >= 0:
            alert()
            (data, count) = get_log_data(file_data, search_word, index, 2, 2)
            print data
        else:
            sys.stdout.write("...")
            sys.stdout.flush()

    index = len(file_data)
    sleep(5)

def alert() :
    print "\n", datetime.datetime.now(), "문제가 발생했습니다!!"

if __name__ == "__main__":
    check("/home/python/python-for-system/로그관리/test.log", "FAIL") 
