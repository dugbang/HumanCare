#!/usr/bin/python

from socket import *
from time import ctime  # time.ctime() 함수를 import. 모듈이름 생략하고 ctime()이름으로 호출가능

HOST = 'localhost'  # 공백으로 두어 bind() 메소드가 아무 가능한 주소를 사용할 수 있게 함
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)  # tcp 서버소켓 할당. 객체생성
tcpSerSock.bind(ADDR)  # - 소켓을 주소로 바인딩
tcpSerSock.listen(5)  # listening 시작. 최대 클라이언트 연결 수 5개

while True:
    print('waiting for connection...')
    tcpCliSock, addr = tcpSerSock.accept()
    print('...connected from:', addr)

    while True:  # -- 클라이언트 연결이 오면 이 dialog 루프로 들어가서 데이터가 수신을 기다림
        data = tcpCliSock.recv(BUFSIZ).decode('utf-8')
        if not data:
            break  # - 클라이언트 메시지가 공백이면 quit하고 다시 wait 상태로
        #tcpCliSock.send(u'[{}] {}'.format(ctime(), data))  # 데이터가 있으면 ctime()값과 data를 송신
        print(data)

    #tcpCliSock.close()  # 클라이언트 세션 종료
tcpSerSock.close()  # - 위 루프가 끝나지 않으므로 이 라인은 실행되지 않는다. just a remainder of close()
