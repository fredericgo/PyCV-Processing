import socket


class ProcessingCanvasClient(object):
	def __init__(self, sock = None):
		if sock is None:
			self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		else:
			self.sock = sock

	def connect(self, host, port):
		self.sock.connect((host, port))

	def sendPoint(self, msg):
		totalsent = 0
		while totalsent < len(msg):
			sent = self.sock.send(msg[totalsent:])
			if sent == 0:
				raise RuntimeError("socket connection broken")
			totalsent += sent

if __name__ == "__main__":
	import random
	pcc = ProcessingCanvasClient()
	pcc.connect("127.0.0.1", 12345)
	msg = " ".join([str(random.randint(0, 255)) for i in range(4)]) + "\n"
	pcc.sendPoint(msg)