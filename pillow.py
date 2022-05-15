from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


class Picture:

    def __init__(self, photo):
        self.photo = Image.open(photo)

    def crop_method(self):
        self.photo = self.photo.resize((1080, 1080))

    def bw(self):
        self.photo = self.photo.convert("L")

    def display(self):
        self.photo.show()

    def watermark(self):
        fonte = ImageFont.truetype(r"arial.ttf", 40)
        ImageDraw.Draw(self.photo).text((900, 1000), "Azamat", font=fonte)

for i in range(1, 4):
    Photos = Picture(f"img{i}.jpg")
    Photos.crop_method()
    Photos.bw()
    Photos.watermark()
    Photos.display()
