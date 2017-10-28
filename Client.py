#!/usr/bin/env python

from socket import *  # -- socket 모듈에서 모든 속성을 import

HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)  # -- tuple

tcpCliSock = socket(AF_INET, SOCK_STREAM)  # socket 함수로 객체 생성
tcpCliSock.connect(ADDR)  # - 서버연결

while True:
    data = input('> ')  # -- 무한루프 시작 및 데이터입력 받기
    if not data:  # -- 입력받은 데이터가 없으면 break
        break
    tcpCliSock.send(data.encode('utf-8'))  # -- 입력받은 데이터 서버로 전송
    #data = tcpCliSock.recv(BUFSIZ)  # --- 서버에서 전송받은 데이터를 data에 저장
    #if not data:
    #    break
    #print(data)

tcpCliSock.close()
