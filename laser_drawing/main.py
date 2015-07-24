from LaserScanner import LaserScanner


class Main(object):
	def __init__(self):
		pass
		
	def setup(self):
		self.ls = LaserScanner()

	def update(self):
		self.ls.update()

	def draw(self):
		"""
			DOC
		"""
		pass

def main():
	m = Main()
	m.setup()
	while True:
		m.update()
		m.draw()

if __name__ == "__main__":
	main()