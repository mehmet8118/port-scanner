# -*- coding: utf-8 -*-
import socket,sys,threading

if len(sys.argv) != 3:
    print("\n\nTwitter: @mehmetserifpasa\nKullanim: python ps.py [Ip] [Port]\n\n")
    sys.exit()


ports=[]

def tara():
    global ports
    ip = sys.argv[1]
    port = int(sys.argv[2])
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((ip,int(port)))
        sock.close()
        ports.append(str(port))
        print("\n\nPort Acik: "+str(port)+"\n\n")
        return True

    except:
        sock.settimeout(3)
        print("[*] Port acik değil : "+str(port))
        sock.close()
        sys.exit()


tara()
