#!/bin/env python
#-*- coding:utf-8 -*-

import mylog
#mylog 모듈 임포트
'''
def printlog(logfile, search_word):
	print "-" * 70
	print "Log file : ",logfile
    print "Find this word : ", search_word
    print "-" * 70
'''


mylog.printlog("/var/log/messages", "fail")
#/var/log/messages 파일에서 fail이라는 단어 찾기