#coding: utf-8

import SimpleHTTPServer
import SocketServer
import os
import sys


def main():
	programName = sys.argv[0]
	currentDir = os.path.join(os.getcwd(), programName)

	if len(sys.argv) > 2 or len(sys.argv) < 2:
		print "EXAMPLE: {} PORT".format(programName)
		sys.exit()
	else:
		PORT = int(sys.argv[1])
		os.system('netsh firewall add allowedprogram program="{}" name="{}" mode=enable scope=all'.format(currentDir, programName))
	
		try:
			Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
			httpd = SocketServer.TCPServer(("", PORT), Handler)
			httpd.serve_forever()
		except Exception, e:
			print "Couldn't Start Webserver :("
			sys.exit()


if __name__ == "__main__":
	main()
