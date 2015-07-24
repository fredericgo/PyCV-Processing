import numpy as np
import cv2

class Cam(object):
	def __init__(self):
		self.cam = cv2.VideoCapture(0)


if __name__ == "__main__":
	cam = Cam()
