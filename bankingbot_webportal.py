import os
import SocketServer

from app import app

if __name__ == '__main__':
	HOST = os.environ.get('SERVER_HOST', '0.0.0.0')
	PORT = 5001
	try:
	    PORT = int(os.environ.get('SERVER_PORT', 5001))
	except ValueError:
		PORT = 5001

	SocketServer.TCPServer.allow_reuse_address = True
	app.debug = False
	app.run(HOST, PORT)