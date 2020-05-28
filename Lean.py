import optparse
import socket
from socket import *


def Connexion(tgthost, tgtport) :
    try :
        skt = socket(AF_INET, SOCK_STREAM)
        skt.connect(tgthost, tgtport)
        skt.send("TestPortDIY\r\n")
        res = skt.recv(100)
        print("Port : " +tgtport+ "Is open")
        print(str(res))
    except :
        print("TCP port is closed sorry mate!!!")


def getPorts(tgthost, tgtports) :
    try :
        tgtip = gethostbyname(tgthost)
        print("Ip of... " + tgthost + " is : " + str(tgtip))
    except :
        print("can't get IP of :" + tgthost)
    try :
        tgthost = gethostbyaddr(tgthost)
        print("resolve result are :  " + str(tgthost))
    except :
        print("can't resolve " + tgthost)

    setdefaulttimeout(2)
    for port in tgtports:
        print("Test port number : " +port)
        Connexion(tgthost,port)

def main() :
    parser = optparse.OptionParser()
    parser.add_option('-H', "--host", dest='tgth', type='string', help='host IP example 127.0.0.1')
    parser.add_option('-P', "--port", dest='tgtp', help='host port Example 25,448,80')
    options, args = parser.parse_args()
    tgtHost = options.tgth
    tgtPort = str(options.tgtp).split(',')
    getPorts(tgtHost, tgtPort)


if __name__ == '__main__' :
    main()
