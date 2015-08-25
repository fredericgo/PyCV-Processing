from Tkinter import Tk, RIGHT, BOTH, GROOVE, Label
from ttk import Frame, Button, Style
from PIL import Image, ImageTk
import cv2

class ImageFrame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.setup()
        self.initUI()
        self.schedule()

    def setup(self):
        self.capture = cv2.VideoCapture(0)


    def initUI(self):
        self.parent.title("Buttons")
        self.style = Style()
        self.style.theme_use("default")

        frame = Frame(self, relief=GROOVE, borderwidth=5)
        frame.pack(fill=BOTH, expand=1)
        self.pack(fill = BOTH, expand = 1)

        self.imageLabel = Label(frame, image = "")
        self.imageLabel.pack(fill=BOTH, expand=1)

        closeButton = Button(self, text="Close")
        closeButton.pack(side=RIGHT)
        okButton = Button(self, text="OK")
        okButton.pack(side=RIGHT)

    def schedule(self):
        def captureImg():
            ret, frame = self.capture.read()
            # Convert the Image object into a TkPhoto object
            b,g,r = cv2.split(frame)
            frame = cv2.merge((r,g,b))
            im = Image.fromarray(frame)
            im = im.resize((640, 480),Image.ANTIALIAS)


            imgtk = ImageTk.PhotoImage(image=im)
            # Put it in the display window
            self.imageLabel.configure(image = imgtk)
            self.imageLabel.image = imgtk
            self.after(100, captureImg)

        self.after(100, captureImg)



def main():

    root = Tk()
    root.geometry("800x600+300+300")
    app = ImageFrame(root)
    root.mainloop()


if __name__ == "__main__":
    main()