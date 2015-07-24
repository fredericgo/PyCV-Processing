import cv2
import numpy as np
from screen_finder.screen_finder import ScreenFinder
from cam import OpenCV_Cam

class LaserScanner(object):
    def __init__(self):
        self.showCamView = True
        self.showTopView = False
        self.screenIsFound = False
        self.captureLaser = False
        self.cam = OpenCV_Cam()
        self.screenFinder = ScreenFinder()

    def findScreen(self):
        self.screenFinder.clear_found()
        while not self.screenIsFound:
            img = self.cam.read()
            self.screenFinder.find_screen_img(img)
            cv2.imshow('camera image', img)
            k = cv2.waitKey(5)
            if k == 27:
                break
        
        cv2.destroyWindow('camera image')

    def setScreenImage(self, bgImage): 
        self.screenFinder.set_screen_img(bgImage)
        self.background = bgImage

    def capture(self):
        if self.captureLaser:
            img = self.cam.read()
            Xcam = self.getLaserLocation(img)
            print Xcam
            #x, y = tuple(self.screenFinder.reverse_transform(Xcam).reshape(-1))
            return Xcam
        

    def update(self):
        self.img = self.cam.read()
        print self.capture()

    def show(self):
        cv2.imshow('Burn this image', self.background)
        if self.showTopView:
            top_view = sf.screen_top_view(img)
            cv2.imshow('Top view', top_view)
        if self.showCamView:
            cv2.imshow('Cam view', self.img)
        

    @staticmethod
    def getLaserLocation(image):
        red_part = image[:,:,2]
        ly, lx = np.unravel_index(red_part.argmax(), red_part.shape)
        return np.array([lx, ly])


if __name__ == "__main__":
    ls = LaserScanner()
    background = cv2.imread('wood_800.png')
    ls.setScreenImage(background)

    while True:
        k = cv2.waitKey(10)
        ls.update()
        ls.show()
        if k == ord('a'):
            sf.find_screen_loop(cam, False)
        elif k == ord('s'):
            background = cv2.imread('wood_800.png')
        elif k == ord('d'):
            ls.show_top_view = not ls.show_top_view
            if show_top_view is False:
                cv2.destroyWindow('Top view')
        elif k == ord('f'):
            ls.show_cam_view = not ls.show_cam_view
            if show_cam_view is False:
                cv2.destroyWindow('Cam view')
        elif k == ord('c'):
            ls.captureLaser = not ls.captureLaser
        elif k == 27:
            break