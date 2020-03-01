#!/bin/env python
#-*- coding: utf-8 -*-

#'모듈 이름.함수' 형식으로 함수를 실행하면 관리하는 로그에서 찾고 싶은 단어를 확인 할 수 있게 한다.
# 타 코드에서 이 모듈을 임포트한다.

def printlog(logfile, search_word, pre_rowcount, next_rowcount):
	f = open(logfile) #logfile 열기
	logdata = f.read() #파일 읽기
	f.close() #파일 닫기

	index = logdata.find(search_word) #찾을 단어의 위치(인덱스) 정보를 알 수 있다.

	if index >= 0 :
	    print "-" * 70
	    print "Log file : ",logfile
        print "Find this word : ", search_word
        #print index #위치 값을 숫자로 출력하고 없으면 -1 출력
        print "-" * 70

        print get_log_data(logdata, index, pre_rowcount, next_rowcount) #로그 추출 함수 호출
        print "-" * 70

#로그 추출을 위한 get_log_data 함수
def get_log_data(logdata, start_index, pre_rowcount, next_rwocount):

	enter_index = max(0, logdata.rfind("n", 0, start_index))
	#찾은 단어의 위치를 중심으로 앞에 줄 바꿈 문자가 있는지 탐색
	#찾고자 하는 단어가 첫 번째 줄에 포함돼 있으면 그 앞에 줄바꿈 문자가 없으므로 enter_index를 max 함수를 이용해 0으로 변경
	'''
	enter_index = logdata.rfind("\n", 0, start_index)
	if enter_index == -1:
		enter_index = 0
	과 동일함'''
    
    for i in range(0, pre_rowcount):
    	enter_index = max(0, logdata.rfind("\n", 0, enter_index)) #

	enter_index2 = logdata.find("\n", start_index, len(logdata))
	#찾은 단어의 위치를 중심으로 뒤에 줄 바꿈 문자가 있는지 탐색
	for i in range(0, next_rowcount):
		next_end_index2 = logdata.find("\n", enter_index2 + 1, len(logdata))
		if next_end_index2 == -1:
			next_end_index2 = enter_index2
			break
		else:
			enter_index2 = next_end_index2
	return logdata[enter_ndex : enter_index2]
	#찾은 단어의 위치를 중심으로 앞의 줄 바꿈 문자와 뒤의 줄 바꿈 문자 사이의 열을 반환

