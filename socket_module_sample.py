#!/bin/env python
#-*- coding:utf-8 -*-

import socket
host= socket.gethostbyname_ex("www.google.com")

#gethostbyname_ex로 전달받은 값 출력
print (u"\n------------HOST 정보 출력-------------")
print host

#for 문을 이용해 값을 한 줄씩 출력
print (u"\n------------HOST 정보를 한 줄씩 출력------------")
for i in host :
    print i

#값에서 마지막 데이터가 IP 목록이므로 그중 첫 번째 주소를 IP로 선택
(hostname, aliaslist, ipaddrlist) = host
print (u"\n-----------IP 주소 선택-------------")
print "ip :", ipaddrlist[0]