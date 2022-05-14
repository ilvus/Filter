from PIL import Image


class Picture:

    def __init__(self, photo):
        self.photo = Image.open(photo)

    def crop_method(self):
        area = (100, 100, 1180, 1180)
        self.photo = self.photo.crop(area)

    def bw(self):
        self.photo = self.photo.convert("L")

    def display(self):
        self.photo.show()


Photos = Picture("dog.jpeg")
Photos.crop_method()
Photos.bw()
Photos.display()

