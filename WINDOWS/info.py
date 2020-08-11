#!/bin/env python
#!-*- coding:utf-8 -*-

import platform
#파이썬 코드 실행하는 운영체제 환경정보 제공 모듈
import multiprocessing
#CPU 갯수 카운트 모듈

print (u"운영체제:"), platform.system()
print (u"운영체제의 상세정보:"), platform.platform()
print (u"운영체제 버전:"), platform.version()
print (u"프로세서정보:"), platform.processor()
print (u"CPU 수:"), multiprocessing.cpu_count()